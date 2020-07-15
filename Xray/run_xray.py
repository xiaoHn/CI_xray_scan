# -*- coding: utf-8 -*-
from Xray.check_port_all import *
import os

def run_xray(port):
    run_status = checkport(port)
    if ('running' == run_status):
         # 运行中
         print("\033[1;3;33m[STATUS]\033[0m " + "\033[36m____*____Scan core is runing____*____\033[0m")
    else:
         # 未运行
         print("\033[1;3;33m[STATUS]\033[0m " + "\033[31m_____Scan core is not runing,start for you now._____\033[0m")
         try:
            xray_pwd = os.getcwd() + '/Xray/bin/'
            proxy_cmd = 'cd ' + xray_pwd + ' && nohup ./xray webscan --listen 0.0.0.0:' + str(port)
            json_cmd = ' --json-output ./Json_result/test.json '
            webhook_cmd = ' --webhook-output http://127.0.0.1:7878/webhook/1 >> run.log 2>&1 &'
            cmd_all = '%s' % (proxy_cmd + json_cmd + webhook_cmd)
            print("\033[36m[INFO]\033[0m " + "\033[32m%s\033[0m" % cmd_all)
            output = str(os.system(cmd_all))
            if(output == '0'):
                print 'OK'
            else:
                print 'Error'

         except KeyboardInterrupt:
            exit("\033[1;3;33m[WARN]\033[0m "+"\033[31m_____You stopped the scanner._____\033[0m")




