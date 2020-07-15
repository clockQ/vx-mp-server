# -*- coding: utf-8 -*-#
# filename: msg/receive.py
import xml.etree.ElementTree as ET
import mt_errs


def parse_xml(web_data):
    """
    解析接受到的粉丝消息
    :param web_data: xml 格式的消息体
    :return:
    """
    if len(web_data) == 0:
        return None

    xml_data = ET.fromstring(web_data)
    msg_type = xml_data.find('MsgType').text.strip('\n').strip()

    try:
        msg_module = __import__('mt_msg.receive')
        receive_file = getattr(msg_module, 'receive')
        msg_obj = getattr(receive_file, f'{msg_type.title()}Msg')
    except AttributeError:
        return ErrMsg(xml_data, mt_errs.UnknownMsgTypeErr(msg_type))
    else:
        return msg_obj(xml_data)


class Msg(object):
    """
    粉丝消息的基类
    """
    def __init__(self, xml_data):
        self.ToUserName = xml_data.find('ToUserName').text.strip('\n').strip()
        self.FromUserName = xml_data.find('FromUserName').text.strip('\n').strip()
        self.CreateTime = xml_data.find('CreateTime').text.strip('\n').strip()
        self.MsgType = xml_data.find('MsgType').text.strip('\n').strip()
        self.MsgId = xml_data.find('MsgId').text.strip('\n').strip()


class ErrMsg(Msg):
    """
    无法正确处理的消息
    """
    def __init__(self, xml_data, err):
        Msg.__init__(self, xml_data)
        self.err = err


class TextMsg(Msg):
    """
    文本型消息
    """
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.Content = xml_data.find('Content').text.strip('\n').strip()


class ImageMsg(Msg):
    """
    图片型消息
    """
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.PicUrl = xml_data.find('PicUrl').text.strip('\n').strip()
        self.MediaId = xml_data.find('MediaId').text.strip('\n').strip()


class VoiceMsg(Msg):
    """
    语音型消息
    """
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.MediaId = xml_data.find('MediaId').text.strip('\n').strip()
        self.Format = xml_data.find('Format').text.strip('\n').strip()
        self.Recognition = xml_data.find('Recognition').text.strip('\n').strip()
