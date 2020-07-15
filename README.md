# CI_xray_scan
#CI调度流程之扫描器模块（目前只适配于甲方的CI自动化构建流程，暂时基于APIDOC数据,具体移步Help）
# Author:Laimooc@拂晓 

## python scanner.py -h
### a) By env and git's name
### ::~proc -> online;test -> test; yf -> yufa
#### ～python scanner.py proc all_git
#### ～python scanner.py yf bbj
#### ～python scanner.py test ybb

### b) By api_change_time on year
##### ～python scanner.py test time:2019
##### ～python scanner.py test time:2019-01
##### ～python scanner.py test time:2020

### c) By host name
##### ～python scanner.py test host:test.baidu.com

### d) By somebody's data on email
##### ～python scanner.py test mail:test_proc@test.com

### e) By is delete
##### ～python scanner.py test deleted
##### ～python scanner.py test undeleted

### f) By is deprecated
##### ～python scanner.py test deprecated
##### ～python scanner.py test undeprecated

### h) By none apidoc and these data need to unique "apiid" eg md5
##### ～python scanner.py test notapiid

## 更多内容移步 https://www.laimooc.cn/
