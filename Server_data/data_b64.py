# -*- coding: utf-8 -*-
from Config.b64_de import *
from Client.env_type import *
from Server_data.repair_data import *

def datas_b64(proxy_port,scan_env, datas):
   if len(str(datas)) < 5:
      return 'Data is none.'
   else:
      for detail in datas:
         apiid = detail.get('apiid', '')
         gitpath = detail.get('gitpath', '')
         reqprotocol = detail.get('reqprotocol', '')
         reqtype = detail.get('reqtype', '')
         reqhost = detail.get(env_host(scan_env), '')
         reqheader = str(detail.get('reqheader', '')).replace(' ', '+')
         requri = str(detail.get('requri', '')).replace(' ', '+')
         reqbody = str(detail.get('reqbody', '')).replace(' ', '+')
         try:
            data_id = datas.index(detail) + 1
            if (str(reqbody)) == 'None':
               try:
                  datas_repair(proxy_port,data_id,apiid,scan_env, reqtype, py_b64(requri), reqhost, reqprotocol, py_b64(reqheader),'')
               except IOError as e:
                  print e
            else:
               try:
                  datas_repair(proxy_port,data_id,apiid,scan_env, reqtype, py_b64(requri), reqhost, reqprotocol, py_b64(reqheader), py_b64(reqbody))
                  #print apiid, gitpath, '>> ' + reqtype, py_b64(requri), reqhost, reqprotocol, py_b64(reqheader), py_b64(reqbody)
               except IOError as e:
                  print e
         except IOError as e:
            print e