# -*- coding: utf-8 -*-
import pycurl
import sys,requests
import StringIO
import urllib3
from Config.user_agent import *
from Config.owner_auth import *
from Dingtalk.dingtalk import *
sys.dont_write_bytecode = True
requests.packages.urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_api_host(scan_env,apiid,requri):
    ua_gent = "User-Agent: " + get_user_agent()
    auth_env = owner_auth(scan_env)
    headers = [ua_gent,auth_env]

    c = pycurl.Curl()
    # 通过curl方法构造一个对象#
    c.fp = StringIO.StringIO()  # 设置IO

    c.setopt(pycurl.REFERER,requri)
    # 设置referer

    c.setopt(pycurl.SSL_VERIFYHOST, False)
    c.setopt(pycurl.SSL_VERIFYPEER, False)
    # 关闭SSL检测

    c.setopt(pycurl.FOLLOWLOCATION, False)
    # 自动进行跳转抓取

    c.setopt(pycurl.MAXREDIRS, 3)
    # 设置最多跳转多少次

    c.setopt(pycurl.CONNECTTIMEOUT, 5)
    # 连接的等待时间，设置为0则不等待

    c.setopt(pycurl.FORBID_REUSE, 1)
    # 完成交互后强制断开连接，不重用 

    c.setopt(pycurl.FRESH_CONNECT,1)
    # 强制获取新的连接，即替代缓存中的连接 

    c.setopt(pycurl.URL, requri)
    # 设置要访问的URL

    c.setopt(pycurl.HTTPHEADER, headers)
    # 传入请求头

    try:
        c.setopt(c.WRITEFUNCTION, c.fp.write)
        # 将返回的内容定向到回调函数crl.fp.write
        c.perform()
        #c.getvalue()
        return ' HTTP-code: ' + str(c.getinfo(c.HTTP_CODE))
        # 返回HTTP状态信息

    except Exception as e:
        error_title = ' Connection-Err:'
        return error_title + str(e)

