# -*- coding: utf-8 -*-
from Config.replace_str import *
from Requests.http_middle import *


def datas_repair(proxy_port,data_id,apiid,scan_env,reqtype,requri,reqhost,reqprotocol,reqheader,reqbody):
    req_host = datas_replace(reqhost)
    req_uri = str(reqprotocol) + '://' + str(req_host) + datas_replace(requri)
    request_api(proxy_port,data_id,apiid,scan_env, reqtype, req_uri, req_host, reqprotocol, reqheader, datas_replace(reqbody))
