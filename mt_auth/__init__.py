from enum import Enum
from mt_util.csv import load_users_by_csv


class Identity(object):
    """
    身份认证信息，记录粉丝的 open ID，和所属角色分组
    """
    def __init__(self, open_id, groups):
        self.open_id = open_id
        self.groups = groups


class Role(Enum):
    SUADMIN = 9999
    ADMIN = 999
    FANS = 2
    VISITORS = 1


def __str2role(string):
    if 'suadmin' == string:
        return Role.SUADMIN
    elif 'admin' == string:
        return Role.ADMIN
    elif 'fans' == string:
        return Role.FANS
    else:
        return Role.VISITORS


__all_users = load_users_by_csv(r'users.csv')


def auth_verify(msg) -> Identity:
    """
    根据粉丝信息中的标识，获取粉丝的权限角色分组
    :param msg: 粉丝消息
    :return: 身份认证信息
    """
    open_id = msg.FromUserName
    find_users = [user for user in __all_users if open_id == user['id']]

    if len(find_users) < 1:
        find_user = [user for user in __all_users if 'unknown' == user['id']][0]
    else:
        find_user = find_users[0]

    groups = [__str2role(group.strip()) for group in find_user['groups'].split('&')]

    return Identity(msg.FromUserName, groups)
