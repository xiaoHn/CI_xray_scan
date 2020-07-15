# coding: UTF-8

import urllib2, time
from datetime import datetime

import socket
start_time = time.time()

try:
    #print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    f = urllib2.urlopen('https://www.baidu.com/', timeout=10)

    code = f.getcode()

    if code < 200 or code >= 300:
        print code



except Exception, e:
    if isinstance(e, urllib2.HTTPError):

        print'http error: {0}'.format(e.code)

    elif isinstance(e, urllib2.URLError) and isinstance(e.reason, socket.timeout):

        print'url error: socket timeout {0}'.format(e.__str__())

    else:

        print'misc error: ' + e.__str__()
#print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

# 试验得知 执行时间太久
end_time = time.time()
duration = end_time - start_time
print duration
