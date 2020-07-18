import requests
import re
import os
import json

BASE_URL = 'https://zhuanlan.zhihu.com'
COLUMNS_API = 'https://www.zhihu.com/api/v4/members/clockQ/column-contributions'
ARTICLES_API = 'https://www.zhihu.com/api/v4/members/clockQ/articles'

LOCK_DB_FILE = 'db.lock'
COLUMNS_FILE = 'columns.json'
ARTICLES_FILE = 'articles.json'
QAS_FILE = 'qas.json'


__headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.116 Safari/537.36"
}


def get_all_columns(columns_api=COLUMNS_API):
    """
    从知乎的后端接口中获得所有的专栏信息
    :param columns_api: 专栏接口
    :return: list[{'title': 标题,,,,},]
    """
    response = requests.get(columns_api, headers=__headers, params={})
    json = response.json()

    next_url = json['paging']['next']
    data = json['data']
    if not data:
        return []

    columns = []
    for sub in data:
        column = sub['column']
        columns.append({
            'title': column['title'],
            'desc': '旻天知乎专栏',
            'comment_permission': column['comment_permission'],
            'url': f'{BASE_URL}/{column["id"]}',
            'created': 0,
            'updated': column['updated'],
            'pic_url': column['image_url'],
        })

    return columns + get_all_columns(next_url)


def get_pic_QA_from_article(article_url):
    """
    从文章中获取第一张配图和内容中的问答dict
    :return: first_png_url, qa_dict
    """
    response = requests.get(article_url, headers=__headers, params={})
    response_text = response.text

    first_png_search = re.search(r'https?://picb.*?\.(jpg|png)', response_text)
    if first_png_search:
        first_png_url = first_png_search.group()
    else:
        first_png_url = ''

    # 使用正则分析出 >问<: ~~~~~~ <答> 中间的内容，
    # 不过不知道为啥，response_text 中总是有两个同样的问题，但有一个的 html 标签是 16 进制编码
    # 没有办法，只能使用 map 去重了
    all_qa = re.finditer(r'&gt;问&lt;：(.*?)&lt;答&gt;', response_text)
    qa_dict = {}
    for qa in all_qa:
        sp = qa.group(1).split('&lt;问&gt;')
        an = sp[0].replace('<b>','').replace('</b>', '')\
            .replace('<p>','').replace('</p>', '\n')\
            .strip('\n')
        qu = sp[1].replace('&gt;答&lt;', '')\
            .replace('<b>', '').replace('</b>', '')\
            .replace('<p>', '').replace('</p>', '\n')\
            .strip('\n')
        # 利用 map 去除重复 question
        qa_dict.setdefault(an, qu)

    return first_png_url, qa_dict


def get_all_articles(articles_api=ARTICLES_API):
    """
    从知乎的后端接口中获得所有的文章信息
    :param articles_api: 文章接口
    :return: articles, qas
        articles:   list[{'title': 标题,,,,},],
        qas:        list[{'title': 'XXX问题', 'text': 'XXX答案'},,,]
    """
    response = requests.get(articles_api, headers=__headers, params={})
    json = response.json()

    next_url = json['paging']['next']
    data = json['data']
    if not data:
        return [], {}

    articles = []
    qas = {}
    for article in data:
        article_url = article['url']
        first_png_url, qa_dict = get_pic_QA_from_article(article_url)
        qas.update(qa_dict)

        articles.append({
            'title': article['title'],
            'desc': article['excerpt'],
            'comment_permission': article['comment_permission'],
            'url': article_url,
            'created': article['created'],
            'updated': article['updated'],
            'pic_url': first_png_url,
        })

    next_articles, next_qas = get_all_articles(next_url)
    qas.update(next_qas)
    return articles + next_articles, qas


all_columns = []
all_articles = []
all_qas = []


def flush_db():
    """
    抓取知乎的专栏、文章和文章内问答信息，并存入文件
    """
    global all_columns
    global all_articles
    global all_qas

    if os.path.exists(LOCK_DB_FILE):
        return None

    # 创建一个文件锁
    with open(LOCK_DB_FILE, 'w') as _:
        pass

    try:
        all_columns = get_all_columns()
        all_articles, all_qas = get_all_articles()

        with open(COLUMNS_FILE, 'w') as f:
            json.dump(all_columns, f, ensure_ascii=False, indent=4)
        with open(ARTICLES_FILE, 'w') as f:
            json.dump(all_articles, f, ensure_ascii=False, indent=4)
        with open(QAS_FILE, 'w') as f:
            json.dump(all_qas, f, ensure_ascii=False, indent=4)
    finally:
        os.remove(LOCK_DB_FILE)


def load_db():
    """
    从本地文件中读取专栏、文章和文章内问答信息
    :return all_columns, all_articles, all_qas
    """
    global all_columns
    global all_articles
    global all_qas

    if not all_columns:
        with open(COLUMNS_FILE, 'r') as f:
            all_columns = json.load(f)
    if not all_articles:
        with open(ARTICLES_FILE, 'r') as f:
            all_articles = json.load(f)
    if not all_qas:
        with open(QAS_FILE, 'r') as f:
            all_qas = json.load(f)

    return all_columns, all_articles, all_qas
