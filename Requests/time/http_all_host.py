
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import pycurl
from datetime import datetime

#print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


start_time = time.time()

url = 'https://www.baidu.com/'
t = Test()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEFUNCTION, t.body_callback)
c.perform()
end_time = time.time()
duration = end_time - start_time
#print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)
#print c.getinfo(pycurl.TOTAL_TIME)
c.close()
print duration
#print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]



