# -*- coding: utf-8 -*-#
# filename: reply.py
import time


class Msg(object):
    def __init__(self, to_user_name, from_user_name):
        self._dict = dict()
        self._dict['ToUserName'] = to_user_name
        self._dict['FromUserName'] = from_user_name

    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, to_user_name, from_user_name, content):
        Msg.__init__(self, to_user_name, from_user_name)
        self._dict['CreateTime'] = int(time.time())
        self._dict['Content'] = content

    def send(self):
        xml_form = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{Content}]]></Content>
            </xml>
            """
        return xml_form.format(**self._dict)


class ImageMsg(Msg):
    def __init__(self, to_user_name, from_user_name, media_id):
        Msg.__init__(self, to_user_name, from_user_name)
        self._dict['CreateTime'] = int(time.time())
        self._dict['MediaId'] = media_id

    def send(self):
        xml_form = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <Image>
                <MediaId><![CDATA[{MediaId}]]></MediaId>
                </Image>
            </xml>
            """
        return xml_form.format(**self._dict)


class NewsMsg(Msg):
    MAX_ARTICLES_COUNT = 8

    class Articles(object):
        def __init__(self, title, desc, pic_url, url):
            self.__dict = dict()
            self.__dict['title'] = title
            self.__dict['desc'] = desc
            self.__dict['pic_url'] = pic_url
            self.__dict['url'] = url

        def send(self):
            xml_form = """
                <item>
                    <Title><![CDATA[{title}]]></Title>
                    <Description><![CDATA[{desc}]]></Description>
                    <PicUrl><![CDATA[{pic_url}]]></PicUrl>
                    <Url><![CDATA[{url}]]></Url>
                </item>
            """
            return xml_form.format(**self.__dict)

    def __init__(self, to_user_name, from_user_name, articles):
        Msg.__init__(self, to_user_name, from_user_name)
        self._dict['CreateTime'] = int(time.time())
        self._dict['Articles'] = articles
        self._dict['ArticleCount'] = len(self._dict['Articles'])

    def send(self):
        articles_xml = ''
        for article in self._dict['Articles']:
            articles_xml += self.Articles(**article).send()

        xml_form = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>{ArticleCount}</ArticleCount>
                <Articles>
                    {articles_xml}
                </Articles>
            </xml>
        """
        return xml_form.format(**self._dict, articles_xml=articles_xml)