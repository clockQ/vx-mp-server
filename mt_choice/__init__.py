import mt_msg.receive as mrc
import mt_msg.reply as mrp


def __get_purpose_by_text():
    pass


def get_purpose_by_msg(identity, msg: mrc.Msg):
    if msg.MsgType == 'text' or msg == 'voice':
        pass
    elif msg.MsgType == 'image':
        pass
    else:
        f"暂且不处理 {msg.MsgType} 类型消息"

    to_user = msg.FromUserName
    from_user = msg.ToUserName

    # if rec_msg.MsgType == 'text':
    #     if rec_msg.Content == '随机':

    #     else:
    #         content = "老板，我不明白你写的什么"
    #         reply_msg = reply.TextMsg(to_user, from_user, content)
    # elif rec_msg.MsgType == 'image':
    #     media_id = rec_msg.MediaId
    #     reply_msg = reply.ImageMsg(to_user, from_user, media_id)
    # else:
    #     content = f"暂时不处理 {rec_msg.MsgType} 类型消息"
    #     reply_msg = reply.TextMsg(to_user, from_user, content)

    return msg


def do(identity, purpose):
    to_user = purpose.FromUserName
    from_user = purpose.ToUserName
    # content = "老板，我不明白你写的什么"
    # reply_msg = mrp.TextMsg(to_user, from_user, content)
    # return reply_msg.send()
    articles = [
        {
            'title': '<物> Docker 到底是什么？',
            'desc': 'Docker(dāo kē)',
            'pic_url': 'https://picb.zhimg.com/80/v2-c86ed02ba9a4f93736573f9ba5ae1e2d_1440w.jpg',
            'url': 'https://zhuanlan.zhihu.com/p/158527476',
        },
    ]
    reply_msg = mrp.NewsMsg(to_user, from_user, articles)
    return reply_msg.send()
