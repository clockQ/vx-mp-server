# -*- coding: utf-8 -*-#
# filename: receive.py
import xml.etree.ElementTree as ET


def parse_xml(web_data):
    """
    解析接受到的粉丝消息
    :param web_data: xml 格式的消息体
    :return:
    """
    if len(web_data) == 0:
        return None

    xml_data = ET.fromstring(web_data)
    msg_type = xml_data.find('MsgType').text

    msg_module = __import__('msg.receive')
    receive_file = getattr(msg_module, 'receive')
    msg_obj = getattr(receive_file, f'{msg_type.title()}Msg')

    return msg_obj(xml_data)


class Msg(object):
    """
    粉丝消息的基类
    """
    def __init__(self, xml_data):
        self.ToUserName = xml_data.find('ToUserName').text
        self.FromUserName = xml_data.find('FromUserName').text
        self.CreateTime = xml_data.find('CreateTime').text
        self.MsgType = xml_data.find('MsgType').text
        self.MsgId = xml_data.find('MsgId').text


class TextMsg(Msg):
    """
    文本型消息
    """
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.Content = xml_data.find('Content').text


class ImageMsg(Msg):
    """
    图片型消息
    """
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.PicUrl = xml_data.find('PicUrl').text
        self.MediaId = xml_data.find('MediaId').text


class VoiceMsg(Msg):
    """
    语音型消息
    """
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.MediaId = xml_data.find('MediaId').text
        self.Format = xml_data.find('Format').text
        self.Recognition = xml_data.find('Recognition').text


