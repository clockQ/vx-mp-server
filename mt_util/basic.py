# -*- coding: utf-8 -*-
# filename: util/basic.py
import os
import urllib.request
import time
import json


class Basic:
    """
    基本类
    """
    sleep_time = 1000

    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0

    def __real_get_access_token(self):
        """
        调用微信api获得 access token
        :return:
        """
        env_dist = os.environ
        app_id = env_dist.get("MP_APP_ID")
        app_secret = env_dist.get("MP_APP_SECRET")
        post_url = (f"https://api.weixin.qq.com/cgi-bin/token?grant_type="
                    f"client_credential&appid={app_id}&secret={app_secret}")
        url_resp = urllib.request.urlopen(post_url)
        url_resp = json.loads(url_resp.read())
        self.__accessToken = url_resp['access_token']
        self.__leftTime = url_resp['expires_in']

    def get_access_token(self):
        """
        返回当时有效的 access token
        :return:
        """
        if self.__leftTime < self.sleep_time:
            self.__real_get_access_token()
        return self.__accessToken

    def run(self):
        """
        简单的线程，保证 token 持续可用
        :return:
        """
        while True:
            if self.__leftTime > self.sleep_time:
                time.sleep(self.sleep_time)
                self.__leftTime -= self.sleep_time
            else:
                self.__real_get_access_token()
