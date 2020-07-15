# -*- coding: utf-8 -*-
from Server_data.pull_data import *
from Xray.run_xray import *


def goscan(scan_env, data_type,proxy_port):
    run_status = checkport(proxy_port)
    if ('running' == run_status):
        # 运行中
        print("\033[1;3;33m[STATUS]\033[0m " + "\033[36m____*____Now scan core is runing.____*____\033[0m")
        pull_datas(proxy_port,scan_env, data_type)
    else:
        run_xray(proxy_port)

