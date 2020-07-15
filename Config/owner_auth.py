# -*- coding: utf-8 -*-
def owner_auth(env_id):
    if (int(env_id) == 1):
        # 环境的auth
        Authorization = 'XDS 3.RyJBUl61znZg2xz9JICoLVI3diaNr653QeN9/4ief5k='
        return Authorization
    elif (int(env_id) == 2):
        Authorization = 'XDS 7.6B30K73gcz4EteFnAas63Q22Qz-Xjhx8sdi3LsSva9U'
        return Authorization
    else:
        Authorization = 'Authorization: XDS 7.3l9gpC4Ad8c_pEWpoT3lcF_DWbgISIqIYHqwOFBFaEE'
        return Authorization