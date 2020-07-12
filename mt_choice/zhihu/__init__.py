import mt_msg.receive as mrc
import mt_msg.reply as mrp


def flush_db(msg: mrc.Msg):
    content = "刷新数据库我还没做呢"
    reply_msg = mrp.TextMsg(msg.FromUserName, msg.ToUserName, content)
    return reply_msg.send()


def random_articles(msg: mrc.Msg):
    articles = [
        {
            'title': '<物> Docker 到底是什么？, 别刷了，就这一篇',
            'desc': 'Docker(dāo kē)',
            'pic_url': 'https://picb.zhimg.com/80/v2-c86ed02ba9a4f93736573f9ba5ae1e2d_1440w.jpg',
            'url': 'https://zhuanlan.zhihu.com/p/158527476',
        },
    ]
    reply_msg = mrp.NewsMsg(msg.FromUserName, msg.ToUserName, articles)
    return reply_msg.send()


def set_question(msg: mrc.Msg):
    content = "出题我还没做呢"
    reply_msg = mrp.TextMsg(msg.FromUserName, msg.ToUserName, content)
    return reply_msg.send()
