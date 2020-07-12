from enum import Enum


class Role(Enum):
    SUADMIN = 9999
    ADMIN = 999
    FANS = 2
    VISITORS = 1


class Identity(object):
    """
    身份认证信息，记录粉丝的 open ID，和所属角色分组
    """
    def __init__(self, open_id, groups):
        self.open_id = open_id
        self.groups = groups


def auth_verify(msg) -> Identity:
    """
    根据粉丝信息中的标识，获取粉丝的权限角色分组
    :param msg: 粉丝消息
    :return: 身份认证信息
    """
    if 'oqtZB1hGCaHD6QWke-vkYAd9k2xE' == msg.FromUserName:
        return Identity(msg.FromUserName, [Role.SUADMIN, Role.ADMIN, Role.FANS])
    else:
        return Identity(msg.FromUserName, [Role.FANS])
