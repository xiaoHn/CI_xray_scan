# -*- coding: utf-8 -*-
import commands
'''
 设置检测端口是否监听函数
'''
def checkport(port):
    cmd2 = str('lsof -i:' + str(port) + "|awk '{print $2}'")
    output = commands.getstatusoutput(cmd2)
    port_pid = output[1].replace('PID', '').strip()
    return port_pid


