# -*- coding: utf-8 -*-

import requests


def push_ftqq(content):
    resp = requests.post("https://sc.ftqq.com/Youtoken.send",data={"text": "vuls notice", "desp": content})
    if resp.json()["errno"] != 0:
        raise ValueError("push ftqq failed, %s" % resp.text)
def push_ftqqss(content):
    resp = requests.post("https://pushbear.ftqq.com/sub",data={"sendkey": "16747-Youtoken","text": "vuls notice", "desp": content})
    #if resp.json()["errno"] != 0:
        #raise ValueError("push ftqq failed, %s" % resp.text)
