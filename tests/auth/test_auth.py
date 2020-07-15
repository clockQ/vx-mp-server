import mt_msg.receive as mrc
import mt_auth


def test_auth_verify():
    to_user_name = 'to_user_name'
    from_user_name = 'from_user_name'
    content = 'content'

    text_msg = f"""
        <xml>
            <ToUserName><![CDATA[{to_user_name}]]></ToUserName>
            <FromUserName><![CDATA[{from_user_name}]]></FromUserName>
            <CreateTime>1594522500</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <MsgId><![CDATA[1594522500]]></MsgId>
            <Content><![CDATA[{content}]]></Content>
        </xml>
    """

    msg_obj = mrc.parse_xml(text_msg)
    result = mt_auth.auth_verify(msg_obj)
    assert result.open_id == from_user_name
    assert result.groups[0] == mt_auth.Role.FANS
