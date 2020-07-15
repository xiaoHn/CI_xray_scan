# -*- coding: utf-8 -*-
import requests
import json

def dingtalk(error_title,error_text,apiid):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=7b40f1ab81d14671f5878a58f69a64b6e1d254f0207d6c9ede4f3c5cd4e10aaa'
    headers = {
        'cache-control': 'no-cache',
        'Content-type': 'application/json',
    }

    datas = {
        "msgtype": "link",
        "link": {
            "text": error_text,
            "title": error_title,
            "picUrl": "http://static.seeyouyima.com/www.meiyou.com/meiyou-bf23e296a9058a8dd5581eda3ea59674.png",
            "messageUrl": "https://apidoc.seeyouyima.com/doc/" + str(apiid)
        }
    }
    try:
        pass
        #requests.post(url, headers=headers, data=json.dumps(datas),verify=False)

    except IOError as e:
        return 'Dingtalk error-' + str(e)

