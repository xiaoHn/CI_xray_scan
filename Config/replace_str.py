# -*- coding: utf-8 -*-
import re

def datas_replace(datas):
    rep = {'test-test-': 'test-', '=value': '=eyJzaWduIjoiMTIzIn0=',":\"value\"": ":\"eyJzaWduIjoiMTIzIn0=\""}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    # print(pattern)
    my_str = pattern.sub(lambda m: rep[re.escape(m.group(0))], datas)
    return my_str


def xray_replace(datas):
    rep = {'none':"","\r\n":"","\n":"","Enabled":"Loaded","sqldet":"sql_injection"}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    # print(pattern)
    my_str = pattern.sub(lambda m: rep[re.escape(m.group(0))], datas)
    return str(my_str).strip()