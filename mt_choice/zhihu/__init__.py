import copy
import random

from fuzzywuzzy import process

import mt_msg.receive as mrc
import mt_msg.reply as mrp
import mt_choice.zhihu.spider as spider


load_db = spider.load_db


def flush_db(msg: mrc.Msg):
    spider.flush_db()
    content = "数据库刷新完成"
    reply_msg = mrp.TextMsg(msg.FromUserName, msg.ToUserName, content)
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


def random_columns(msg: mrc.Msg):
    all_columns_title = [columns['title'] for columns in spider.all_columns]
    text = __get_text_from_msg(msg)
    extract_result = process.extractOne(text[4:], all_columns_title)
    # 匹配率大于 10% 的返回指定专栏
    if extract_result[1] > 10:
        columns_index = all_columns_title.index(extract_result[0])
        column = spider.all_columns[columns_index:columns_index+1]
        reply_msg = mrp.NewsMsg(msg.FromUserName, msg.ToUserName, column)
        return reply_msg.send()

    # 否则返回随机专栏
    else:
        columns_count = len(all_columns_title)
        rd_num = random.randint(1, columns_count)
        columns = spider.all_columns[rd_num-1:rd_num]
        reply_msg = mrp.NewsMsg(msg.FromUserName, msg.ToUserName, columns)
        return reply_msg.send()


def random_articles(msg: mrc.Msg):
    articles_count = len(spider.all_articles)
    rd_num = random.randint(0, articles_count-1)
    articles = copy.copy(spider.all_articles[rd_num])
    articles['title'] = '[随机文章] ' + articles['title']
    reply_msg = mrp.NewsMsg(msg.FromUserName, msg.ToUserName, [articles])
    return reply_msg.send()


def specify_articles(msg: mrc.Msg):
    all_articles_title = [articles['title'] for articles in spider.all_articles]
    text = __get_text_from_msg(msg)
    extract_result = process.extractOne(text[4:], all_articles_title)

    # 匹配率大于 50% 的返回指定文章
    if extract_result[1] > 50:
        articles_index = all_articles_title.index(extract_result[0])
        articles = spider.all_articles[articles_index:articles_index+1]
        reply_msg = mrp.NewsMsg(msg.FromUserName, msg.ToUserName, articles)
        return reply_msg.send()

    # 否则返回随机文章
    else:
        return random_articles(msg)


__user_qa = {}


def random_question(msg: mrc.Msg):
    global __user_qa

    all_questions = list(spider.all_qas.keys())
    question_count = len(all_questions)

    rd_num = random.randint(0, question_count-1)
    question = all_questions[rd_num]
    __user_qa[msg.FromUserName] = question

    reply_msg = mrp.TextMsg(msg.FromUserName, msg.ToUserName, '[随机问题] ' + question)
    return reply_msg.send()


def specify_question(msg: mrc.Msg):
    global __user_qa

    all_question = spider.all_qas.keys()
    text = __get_text_from_msg(msg)
    extract_result = process.extractOne(text[4:], all_question)

    # 匹配率大于 50% 的返回指定问题
    if extract_result[1] > 50:
        __user_qa[msg.FromUserName] = extract_result[0]
        reply_msg = mrp.TextMsg(msg.FromUserName, msg.ToUserName, extract_result[0])
        return reply_msg.send()

    # 否则返回随机问题
    else:
        return random_question(msg)


def get_answer(msg: mrc.Msg):
    global __user_qa

    question = __user_qa.get(msg.FromUserName)
    answer = spider.all_qas.get(question, "你先说 “出题”")
    reply_msg = mrp.TextMsg(msg.FromUserName, msg.ToUserName, answer)
    return reply_msg.send()
