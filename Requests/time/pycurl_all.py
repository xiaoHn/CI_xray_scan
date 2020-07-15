# -*- coding: utf-8 -*-
import pycurl, urllib, time
from io import BytesIO
from datetime import datetime
start_time = time.time()

#print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

url = 'https://www.baidu.com/'
headers = ["User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
]
data = {
    "data": "eyJ0cyI6MTUzNDMyMjMyOCwiZGF0YWluZm8iOiJ7XCJVaWRcIjoyMjR9Iiwic2lnbiI6IkZFRjdCQjdBODNBOUJDNjkzQkIzQ0YzMDEyQ0JBRjE1In0","trade": ""
}
c = pycurl.Curl()
# 通过curl方法构造一个对象#

c.setopt(pycurl.REFERER,'http://www.baidu.com/test.html')
# 设置referer

c.setopt(pycurl.FOLLOWLOCATION, True)
# 自动进行跳转抓取

c.setopt(pycurl.MAXREDIRS, 5)
# 设置最多跳转多少次

c.setopt(pycurl.CONNECTTIMEOUT, 3)
# 设置链接超时

#c.setopt(pycurl.TIMEOUT, 120)
# 下载超时

c.setopt(pycurl.ENCODING, 'gzip,deflate')
# 处理gzip内容#

c.setopt(c.PROXY,'127.0.0.1:8080')
# 代理

c.setopt(pycurl.FORBID_REUSE, 1)
# 完成交互后强制断开连接，不重用 

c.setopt(pycurl.FRESH_CONNECT,1)
# 强制获取新的连接，即替代缓存中的连接 

c.setopt(pycurl.DNS_CACHE_TIMEOUT,60)
# 设置保存DNS信息的时间，默认为120秒

c.fp = BytesIO()
c.setopt(pycurl.URL, url)
# 设置要访问的URL

c.setopt(pycurl.HTTPHEADER, headers)
# 传入请求头

#c.setopt(pycurl.POST, 1)
#c.setopt(pycurl.POSTFIELDS, urllib.urlencode(data))
# 传入POST数据

c.setopt(c.WRITEFUNCTION, c.fp.write)
# 回调写入字符串缓存

c.perform()

code = c.getinfo(c.RESPONSE_CODE)
# 返回响应状态码


html = c.fp.getvalue()
# 返回源代码 

totaltime = c.getinfo(c.TOTAL_TIME)
# 上一请求总的时间

#print code
#print c.getinfo(pycurl.TOTAL_TIME)
#print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
end_time = time.time()
duration = end_time - start_time
print duration

