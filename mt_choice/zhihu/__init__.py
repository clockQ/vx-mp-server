import random
import mt_msg.receive as mrc
import mt_msg.reply as mrp
import mt_choice.zhihu.spider as spider
from fuzzywuzzy import process


load_db = spider.load_db


def flush_db(msg: mrc.Msg):
    spider.flush_db()
    content = "数据库刷新完成"
    reply_msg = mrp.TextMsg(msg.FromUserName, msg.ToUserName, content)
    return reply_msg.send()


def get_columns(msg: mrc.Msg):
    reply_msg = mrp.NewsMsg(msg.FromUserName, msg.ToUserName, spider.all_columns)
    return reply_msg.send()


def __get_text_from_msg(msg: mrc.Msg):
    # 重新获得用户输入
    if msg.MsgType == 'text':
        text = msg.Content
    elif msg.MsgType == 'voice':
        text = msg.Recognition
    else:
        text = '随机'
    return text


def random_articles(msg: mrc.Msg):
    all_articles_title = [articles['title'] for articles in spider.all_articles]
    text = __get_text_from_msg(msg)
    extract_result = process.extractOne(text, all_articles_title)

    # 匹配率大于 50% 的返回指定文章
    if extract_result[1] > 50:
        articles_index = all_articles_title.index(extract_result[0])
        article = spider.all_articles[articles_index:articles_index+1]
        reply_msg = mrp.NewsMsg(msg.FromUserName, msg.ToUserName, article)
        return reply_msg.send()

    # 否则返回随机文章
    else:
        articles_count = len(all_articles_title)
        rd_num = random.randint(1, articles_count)
        articles = spider.all_articles[rd_num-1:rd_num]
        reply_msg = mrp.NewsMsg(msg.FromUserName, msg.ToUserName, articles)
        return reply_msg.send()


__user_qa = {}


def set_question(msg: mrc.Msg):
    global __user_qa

    all_question = spider.all_qas.keys()
    text = __get_text_from_msg(msg)
    extract_result = process.extractOne(text, all_question)

    __user_qa[msg.FromUserName] = extract_result[0]
    reply_msg = mrp.TextMsg(msg.FromUserName, msg.ToUserName, extract_result[0])
    return reply_msg.send()


def get_answer(msg: mrc.Msg):
    global __user_qa

    question = __user_qa.get(msg.FromUserName)
    answer = spider.all_qas.get(question, "你先说 “出题”")
    reply_msg = mrp.TextMsg(msg.FromUserName, msg.ToUserName, answer)
    return reply_msg.send()
