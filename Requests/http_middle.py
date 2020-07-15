# -*- coding: utf-8 -*-
from Config.xxf_ip import *
from Requests.check_host import *
from requests.adapters import HTTPAdapter
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))

def request_api(port,data_id,apiid,scan_env,reqtype,requri,reqhost,reqprotocol,reqheader,reqbody):
    # 接口数据拉取出来后分配的id
    data_id = 'Rid: ' + str(data_id)

    # 数据库重的Authorization
    myclientnum = reqheader.find('myclient')
    req_header = reqheader[:myclientnum-1]

    # 自定义Authorization
    Authorization = owner_auth(scan_env)

    proxys = {
        "https":"127.0.0.1:"+str(port),
        "http":"127.0.0.1:"+str(port)
    }

    headers = {
        "Host": reqhost,
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': get_user_agent(),
        'Accept': 'application/json,text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://'+reqhost +'/',
        'Origin': 'http://'+reqhost +'/',
        'Connection': 'close',
        "myclient": '0150050000000000',
        'Authorization': Authorization,
        'statinfo': 'eyJvc2RldmljZSI6Ikd1ZXNzLWJhYmEiLCJvbmx5a2V5IjoiODY1MDIxMzM0MTQwMTMwIiwib3Ntb2RlbCI6Ikd1ZXNzLWJhYmEiLCJ1bWVuZ21hYyI6IjAwOjUxOjEwOmYwOmQ1OmFhIiwib3MiOjEsIm90Ijoid2hvIGFyZSB5b3UiLCJvc2JyYW5kIjoiSmlhb2JhYmEiLCJpZGZhIjoiODY1MDIxMzM0MTQwMTMwIiwiaW1laSI6Ijg2NTAyMTMzNDE0MDEzMCIsImltc2kiOiI0NjAwMDEyMzQ1Njc4OTAiLCJ1YSI6Ikd1ZXNzLWJhYmEiLCJvcGVudWRpZCI6ImJuMjYxMzRhLTE3MTEtMDA2Ni1hZmZmLWNhZTlhZG1pbm91IiwibWFjIjoiMDA6NTE6MTA6ZjA6ZDU6YWEiLCJtYW51ZmFjdHVyZXIiOiJZVUFOTEFPIiwic2RrdmVyc2lvbiI6MjIsIm1hY19yZWFsIjoiMDA6NTE6MTA6ZjA6ZDU6YWEiLCJzZXJpYWwiOiIxMjM0NTY3MCIsImJ1aWxkdiI6IjEwMC45LjkiLCJpZGZhIjoiODY1MDIxMzM0MTQwMTMwIiwiaW1zaSI6IjQ2MDAwMTIzNDU2Nzg5MCIsImltZWkiOiI4NjUwMjEzMzQxNDAxMzAiLCJvc3ZlcnNpb24iOiI5LjkuMCIsInVtZW5naWQiOiI4NjUwMjEzMzQxNGJhYmEiLCJyb212ZXJzaW9uIjoiIiwib3NuYW1lIjoiYmFiYXBhaSIsImFuZHJvaWRpZCI6Ijg2NTAyMTMzNDE0YmFiYSIsImFwbiI6IjQiLCJ1aWQiOjEwMDAwMDAwMCwiZG5hIjoiYzIzYmEyODE0OGNkNjJjYzg1YjRlZDdlMWUxNGQ3Zjg3NjhhNTI4NzAzODQ5NTZkYTc1NmI3YzkwYjY0NDNmZSIsInNvdXJjZSI6IkNvbW11bml0eURpc3BhdGNoRnJhZ21lbnQ6U2VleW91QWN0aXZpdHktJmd0O1dlYlZpZXdGcmFnbWVudDpXZWJWaWV3QWN0aXZpdHkiLCJjaGFubmVsaWQiOiJiYWJhIiwidiI6IjcuOS44IiwidXRkaWQiOiJYQTAwTU5RRnVjQUNkZU9zWmFGdTFxaGkifQ==',
        'source': 'CommunityDispatchFragment:SeeyouActivity->WebViewFragment:WebViewActivity',
        'elder': '5L2g5p+l5LiN5Yiwh03mcao00piv6LCB55qE5ZOm',
        'client': '0',
        'version': '7.9.3',
        'X-Forwarded-For': xxf_ip(),
        'uuid': 'av261bmy-2019-0022-aefe-c3e88074admin',
        'cookie': 'session_id: sorrybmy-2019-0022-aefe-c3e88074admin'
    }

    try:
        req_type = reqtype.strip().lower()
        check_host_result = str(check_api_host(scan_env,apiid,requri))
        if 'HTTP-code' in check_host_result:
            check_host_result = check_host_result.replace('HTTP-code','Check-code')
            print data_id + check_host_result + ' ' + reqtype,requri + ' Transit_port-' + str(port)
            if 'get' in req_type:
                response_get = requests.get(requri, headers=headers, verify=False, timeout=5,allow_redirects=False)
                if(response_get.status_code == 200):
                    print data_id + ' ' + 'Request-code: ' + str(response_get.status_code) + ' ' + reqtype, requri + ' Go in proxy '
                    requests.get(requri, headers=headers, verify=False, timeout=5, allow_redirects=False,proxies=proxys)
                else:
                    error_text_http = 'GET预请求异常，请从apidoc纠察！' + requri
                    error_title_http = 'HTTP-code ==' + str(response_get.status_code)
                    dingtalk(error_title_http,error_text_http,apiid)

            elif 'post' in req_type:
                response_post = requests.post(requri, headers=headers, data=reqbody, verify=False, timeout=5, allow_redirects=False)
                if(response_post.status_code == 200):
                    print data_id + ' ' + 'Request-code: ' + str(response_post.status_code) + ' ' + reqtype, requri + ' Go in proxy '
                    requests.post(requri, headers=headers, data=reqbody, verify=False, timeout=5, allow_redirects=False,proxies=proxys)
                else:
                    error_text_http = 'POST预请求异常，请从apidoc纠察！' + requri
                    error_title_http = 'HTTP-code ==' + str(response_post.status_code)
                    dingtalk(error_title_http,error_text_http,apiid)

            elif 'put' in req_type:
                response_put = requests.put(requri, headers=headers, data=reqbody, verify=False,timeout=5, allow_redirects=False)
                if (response_put.status_code == 200):
                    print data_id + ' ' + 'Request-code: ' + str(response_put.status_code) + ' ' + reqtype, requri + ' Go in proxy '
                    requests.put(requri, headers=headers, data=reqbody, verify=False, timeout=5, allow_redirects=False, proxies=proxys)
                else:
                    error_text_http = 'PUT预请求异常，请从apidoc纠察！' + requri
                    error_title_http = 'HTTP-code ==' + str(response_put.status_code)
                    dingtalk(error_title_http,error_text_http,apiid)
            elif 'delete' in req_type:
                response_delete = requests.delete(requri, headers=headers, data=reqbody, verify=False, timeout=5, allow_redirects=False)
                if (response_delete.status_code == 200):
                    print data_id + ' ' + 'Request-code: ' + str(response_delete.status_code) + ' ' + reqtype, requri + ' Go in proxy '
                    requests.delete(requri, headers=headers, data=reqbody, verify=False, timeout=5, allow_redirects=False, proxies=proxys)
                else:
                    error_text_http = 'DELETE预请求异常，请从apidoc纠察！' + requri
                    error_title_http = 'HTTP-code ==' + str(response_delete.status_code)
                    dingtalk(error_title_http,error_text_http,apiid)
            elif 'patch' in req_type:
                response_patch = requests.patch(requri, headers=headers, data=reqbody, verify=False, timeout=5, allow_redirects=False)
                if(response_patch.status_code == 200):
                    print data_id + ' ' + 'Request-code: ' + str(response_patch.status_code) + ' ' + reqtype, requri + ' Go in proxy '
                    requests.patch(requri, headers=headers, data=reqbody, verify=False, timeout=5, allow_redirects=False, proxies=proxys)
                else:
                    error_text_http = 'PATCh预请求异常，请从apidoc纠察！' + requri
                    error_title_http = 'HTTP-code ==' + str(response_patch.status_code)
                    dingtalk(error_title_http,error_text_http,apiid)
            else:
                return 'hello error'
        elif 'Connection-Err' in check_host_result:
            print data_id + ' ' + apiid + ' ' + requri + ' ' + check_host_result
            error_title = ' Host Connection-Err:'
            error_text = check_host_result
            # 钉钉通知异常接口
            dingtalk(error_title, error_text, apiid)
        else:
            print 'Unerror-' + data_id + ' ' + apiid + ' ' + requri + ' ' + check_host_result
    except IOError as e:
        print 'host error:' + data_id + ' ' + apiid + ' ' + requri + ' ' + reqtype + str(e)
