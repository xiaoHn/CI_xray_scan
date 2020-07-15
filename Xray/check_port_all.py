# -*- coding: utf-8 -*-
import commands
'''
 设置检测端口是否监听函数
'''

def checkport(port):
    cmd0 = str('lsof -i:' + str(port) + "|grep xray")
    output = commands.getstatusoutput(cmd0)
    if 'xray' in str(output):
        return 'running'
    else:
        return 'not-running'