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
        return f"暂时不能处理 '{self.mapping.get(self.msg_type, self.msg_type)}'"


class FileLockErr(MtErr):
    def __str__(self):
        return f"文件上锁，无法执行"


class ZhiHuErr(MtErr):
    def __init__(self, err_code, err_msg):
        self.err_code = err_code
        self.err_msg = err_msg

    def __str__(self):
        return f'知乎函数异常，错误码：{self.err_code}, 错误信息：{self.err_msg}'
