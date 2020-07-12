# -*- coding: utf-8 -*-
# filename: handle.py
import web
import hashlib

import mt_msg.receive as mrc
import mt_choice
import mt_auth
from mt_errs import UnknownMsgTypeErr


class Handle(object):
    # 和微信公众号后台配置的 TOKEN 要一致
    TOKEN = "MinTianClockToken"

    def GET(self):
        try:
            data = web.input()
            print(f"handle/GET 接受参数 {data}")

            if len(data) == 0:
                return "后端接口已启动"

            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr

            # hash 签名验证
            lst = [self.TOKEN, timestamp, nonce]
            lst.sort()
            sha1 = hashlib.sha1()
            for lst in lst:
                sha1.update(lst.encode('utf-8'))
            hashcode = sha1.hexdigest()
            print(f"handle/GET 签名结果: hashcode={hashcode}, signature={signature}")

            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as err:
            print(f"handle/GET {type(err)} 异常, msg => {err}")
            return err

    def POST(self):
        try:
            data = web.data()
            print(f"handle/POST 接受参数 {data}")

            # 消息处理
            rec_msg = mrc.parse_xml(data)
            if rec_msg is None:
                return 'success'

            # 根据用户信息获取粉丝角色
            role = mt_auth.auth_verify(rec_msg)
            # 根据消息获得用户行为
            purpose = mt_choice.get_purpose_by_msg(rec_msg)
            # 根据用户行为执行响应动作
            return mt_choice.do(purpose)
        except (UnknownMsgTypeErr, Exception) as err:
            print(f"handle/POST {type(err)} 异常, msg => {err}")
            return err
