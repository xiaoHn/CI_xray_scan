# -*- coding: utf-8 -*-
import time
import requests
start_time = time.time()
try:
    response_get = requests.get('https://www.baidu.com/')
except:
    print e
# 试验得知 执行时间太久
end_time = time.time()
duration = end_time - start_time
print duration
