# -*- coding: utf-8 -*-
import requests
import json

def dingtalk(error_title,error_text,apiid):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=Youtoken'
    headers = {
        'cache-control': 'no-cache',
        'Content-type': 'application/json',
    }

    datas = {
        "msgtype": "link",
        "link": {
            "text": error_text,
            "title": error_title,
            "picUrl": "http://static.test.com/www.mtestu.com/test-bf23e296a9058a8dd5581eda3ea59674.png",
            "messageUrl": "https://apidoc.test.com/doc/" + str(apiid)
        }
    }
    try:
        pass
        #requests.post(url, headers=headers, data=json.dumps(datas),verify=False)

    except IOError as e:
        return 'Dingtalk error-' + str(e)

