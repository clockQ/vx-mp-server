import mt_msg.receive as mrc
import mt_msg.reply as mrp
from mt_auth import Role
from mt_choice import zhihu

zhihu.load_db()

all_purpose = {
    '刷新数据库': (zhihu.flush_db, [Role.SUADMIN]),
    '随机专栏': (zhihu.random_columns, [Role.SUADMIN]),
    '随机文章': (zhihu.random_articles, [Role.FANS]),
    '给我一篇': (zhihu.specify_articles, [Role.FANS]),
    '随机出题': (zhihu.set_question, [Role.FANS]),
    '给我一道': (zhihu.set_question, [Role.FANS]),
    '给我答案': (zhihu.get_answer, [Role.FANS]),
}


def unknow_purpose(msg: mrc.Msg):
    mapping = {
        'text': '老板，我不明白你写的什么',
        'image': '老板，我这智商也就告别图片了',
        'voice': '老板，我不明白你说的什么',
        'video': '老板，我这智商也就告别视频了',
        'shortvideo': '老板，我这智商也就告别短视频了',
        'location': '老板，你给我发地址也没有用啊',
        'link': '老板，这个链接是让我学习的吗',
    }

    return mrp.TextMsg(msg.FromUserName, msg.ToUserName, mapping[msg.MsgType]).send()


def permission_denied_purpose(msg: mrc.Msg):
    content = '权限不足，请联系管理员开通'
    return mrp.TextMsg(msg.FromUserName, msg.ToUserName, content).send()
