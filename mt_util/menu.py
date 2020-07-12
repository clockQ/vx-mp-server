# -*- coding: utf-8 -*-
# filename: util/menu.py
import urllib.request
from mt_util.basic import Basic


"""
权限不足，无法使用
"""


class Menu(object):
    def __init__(self):
        pass

    def create(self, post_data, access_token):
        post_url = "https://api.weixin.qq.com/cgi-bin/menu/addconditional?access_token=%s" % access_token
        post_data = post_data.encode('utf-8')
        url_resp = urllib.request.urlopen(url=post_url, data=post_data)
        print(url_resp.read())

    def query(self, access_token):
        post_url = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % access_token
        url_resp = urllib.request.urlopen(url=post_url)
        print(url_resp.read())

    def delete(self, access_token):
        post_url = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % access_token
        url_resp = urllib.request.urlopen(url=post_url)
        print(url_resp.read())

    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self, access_token):
        post_url = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % access_token
        url_resp = urllib.request.urlopen(url=post_url)
        print(url_resp.read())


if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button": [
            {
                "type": "click", 
                "name": "今日歌曲", 
                "key": "V1001_TODAY_MUSIC"
            }, 
            {
                "name": "菜单", 
                "sub_button": [
                    {
                        "type": "view", 
                        "name": "搜索", 
                        "url": "http://www.soso.com/"
                    }, 
                    {
                        "type": "miniprogram", 
                        "name": "wxa", 
                        "url": "http://mp.weixin.qq.com", 
                        "appid": "wx286b93c14bbf93aa", 
                        "pagepath": "pages/lunar/index"
                    }, 
                    {
                        "type": "click", 
                        "name": "赞一下我们", 
                        "key": "V1001_GOOD"
                    }
                ]
            }
        ], 
        "matchrule": {
            "tag_id": "2", 
            "sex": "1", 
            "country": "中国", 
            "province": "广东", 
            "city": "广州", 
            "client_platform_type": "2", 
            "language": "zh_CN"
        }
    }
    """
    accessToken = Basic().get_access_token()
    #myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)
