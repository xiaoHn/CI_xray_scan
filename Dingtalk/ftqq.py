# -*- coding: utf-8 -*-

import requests


def push_ftqq(content):
    resp = requests.post("https://sc.ftqq.com/SCU69492Te3ed88766d48ccec1912edccfe2537b35df9f19ae62ad.send",data={"text": "vuls notice", "desp": content})
    if resp.json()["errno"] != 0:
        raise ValueError("push ftqq failed, %s" % resp.text)
def push_ftqqss(content):
    resp = requests.post("https://pushbear.ftqq.com/sub",data={"sendkey": "16747-a420c7eb8a0f24f42ea49baed26326b1","text": "vuls notice", "desp": content})
    #if resp.json()["errno"] != 0:
        #raise ValueError("push ftqq failed, %s" % resp.text)
