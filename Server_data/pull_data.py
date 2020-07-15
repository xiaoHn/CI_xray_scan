# -*- coding: utf-8 -*-
from Config.database import *
from Server_data.scan_type_sql import *
from Server_data.data_b64 import *

def pull_datas(proxy_port,scan_env,scan_type):
   mysql = Database()
   try:
      querySql = scan_type_dict(scan_env,scan_type)
      print querySql
      datas = mysql.query(querySql)
      return datas_b64(proxy_port,scan_env,datas)

   except Exception, e:
      print e
