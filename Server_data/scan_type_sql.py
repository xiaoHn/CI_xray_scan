# -*- coding: utf-8 -*-

def scan_type_dict(env_id,data_type):
    # 删除
    if 'deleted' == data_type:
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where is_delete =1;"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where is_delete =1;"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where is_delete =1;"
            return sql
        else:
            pass
    # 未删除
    elif 'undeleted' == data_type:
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where is_delete !=1;"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where is_delete !=1;"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where is_delete !=1;"
            return sql
        else:
            pass

    # 废弃
    elif 'deprecated' == data_type:
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where is_deprecated =1;"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where is_deprecated =1;"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where is_deprecated =1;"
            return sql
        else:
            pass

    # 未废弃
    elif 'undeprecated' == data_type:
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where is_deprecated !=1;"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where is_deprecated !=1;"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where is_deprecated !=1;"
            return sql
        else:
            pass

    # 开发者邮箱
    elif ('mail:' in data_type) or ('@xiaoyouzi.com' in data_type) :
        data_type = str(data_type).replace('mail:','')
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where cname_email = '" + data_type + "';"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where cname_email = '" + data_type + "';"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where cname_email = '" + data_type + "';"
            return sql
        else:
            pass

    # apidoc数据
    elif 'apiid' == data_type:
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where apiid not like '%not_apiid%';"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where apiid not like '%not_apiid%';"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where apiid not like '%not_apiid%';"
            return sql
        else:
            pass

    # 非apidoc数据
    elif 'notapiid' == data_type:
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where apiid like '%not_apiid%';"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where apiid like '%not_apiid%';"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where apiid like '%not_apiid%';"
            return sql
        else:
            pass

    # api最后改变时间
    elif 'time:' in data_type:
        data_type = str(data_type).replace('time:','')
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where api_change_time like '%" + data_type + "%';"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where api_change_time like '%" + data_type + "%';"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where api_change_time like '%" + data_type + "%';"
            return sql
        else:
            pass

    # 依据host
    elif 'host:' in data_type:
        data_type = str(data_type).replace('host:','')
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where reqhost_online like '%" + data_type + "%';"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where reqhost_yf like '%" + data_type + "%';"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where reqhost_test like '%" + data_type + "%';"
            return sql
        else:
            pass

    # git所有地址
    elif 'all_git' in data_type:
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where 1;"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where 1;"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where 1;"
            return sql
        else:
            pass

    # git地址类
    else:
        if (int(env_id) == 3):
            sql = "select reqprotocol,gitpath,reqhost_online,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where gitpath like '%" + data_type + "%';"
            return sql
        elif (int(env_id) == 2):
            sql = "select reqprotocol,gitpath,reqhost_yf,requri,((reqheader)),reqbody,reqtype,apiid from as_requestdata where gitpath like '%" + data_type + "%';"
            return sql
        elif (int(env_id) == 1):
            sql = "select reqprotocol,gitpath,reqhost_test,requri,reqheader,reqbody,reqtype,apiid from as_requestdata where gitpath like '%" + data_type + "%';"
            return sql
        else:
            pass