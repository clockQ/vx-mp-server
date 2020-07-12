class MtErr(Exception):
    def __str__(self):
        pass


class UnknownMsgTypeErr(MtErr):
    mapping = {
        'text': '文本消息',
        'image': '图片消息',
        'voice': '语音消息',
        'video': '视频消息',
        'shortvideo': '小视频消息',
        'location': '地理位置消息',
        'link': '链接消息',
    }

    def __init__(self, msg_type):
        self.msg_type = msg_type

    def __str__(self):
        return f"暂时不能处理 {self.mapping.get(self.msg_type, self.msg_type)} 类型消息"
