from enum import Enum


class Role(Enum):
    SUADMIN = 0
    ADMIN = 1
    FANS = 100
    VISITORS = 200


class Identity(object):
    """
    记录粉丝的 open ID，和可访问范围
    """
    def __init__(self, open_id, scope):
        self.open_id = open_id
        self.scope = scope


def auth_verify(msg) -> Identity:
    if 'oqtZB1hGCaHD6QWke-vkYAd9k2xE' == msg.FromUserName:
        return Identity(msg.FromUserName, [Role.SUADMIN, Role.ADMIN, Role.FANS])
    else:
        return Identity(msg.FromUserName, [Role.FANS])
