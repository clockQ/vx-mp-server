import msg.receive as mrc


def test_process_text_msg():
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
    assert msg_obj.ToUserName == to_user_name
    assert msg_obj.FromUserName == from_user_name
    assert msg_obj.Content == content


def test_process_image_msg():
    to_user_name = 'to_user_name'
    from_user_name = 'from_user_name'
    pic_url = 'pic_url'
    media_id = 'media_id'

    text_msg = f"""
        <xml>
            <ToUserName><![CDATA[{to_user_name}]]></ToUserName>
            <FromUserName><![CDATA[{from_user_name}]]></FromUserName>
            <CreateTime>1594522500</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <MsgId><![CDATA[1594522500]]></MsgId>
            <PicUrl><![CDATA[{pic_url}]]></PicUrl>
            <MediaId><![CDATA[{media_id}]]></MediaId>
        </xml>
    """

    msg_obj = mrc.parse_xml(text_msg)
    assert msg_obj.ToUserName == to_user_name
    assert msg_obj.FromUserName == from_user_name
    assert msg_obj.PicUrl == pic_url
    assert msg_obj.MediaId == media_id


def test_process_voice_msg():
    to_user_name = 'to_user_name'
    from_user_name = 'from_user_name'
    media_id = 'media_id'
    recognition = 'recognition'

    text_msg = f"""
        <xml>
            <ToUserName><![CDATA[{to_user_name}]]></ToUserName>
            <FromUserName><![CDATA[{from_user_name}]]></FromUserName>
            <CreateTime>1594522500</CreateTime>
            <MsgType><![CDATA[voice]]></MsgType>
            <MsgId>6848421990236160000</MsgId>
            <MediaId><![CDATA[{media_id}]]></MediaId>
            <Format><![CDATA[amr]]></Format>
            <Recognition><![CDATA[{recognition}]]></Recognition>
        </xml>>
    """

    msg_obj = mrc.parse_xml(text_msg)
    assert msg_obj.ToUserName == to_user_name
    assert msg_obj.FromUserName == from_user_name
    assert msg_obj.MediaId == media_id
    assert msg_obj.Recognition == recognition
