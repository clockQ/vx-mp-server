class Role(object):
    """
    记录粉丝的 open ID，和可访问范围
    """
    def __init__(self, open_id, scope):
        self.open_id = open_id
        self.scope = scope


def auth_verify(msg) -> Role:
    pass
