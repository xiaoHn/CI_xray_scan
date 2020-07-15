# coding: UTF-8

import StringIO
import time
import pycurl
from datetime import datetime


import os

start_time = time.time()

class Test:

    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def test_gzip(input_url):
    #print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    t = Test()


    c = pycurl.Curl()

    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)

    c.setopt(pycurl.ENCODING, 'gzip')

    c.setopt(pycurl.URL, input_url)

    c.perform()

    http_code = c.getinfo(pycurl.HTTP_CODE)

    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)

    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)

    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)

    http_total_time = c.getinfo(pycurl.TOTAL_TIME)

    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)

    #print 'http_code http_size conn_time pre_tran start_tran total_time'

    #print "%d %d %f %f %f %f" % (http_code, http_size, http_conn_time, http_pre_tran, http_start_tran, http_total_time)


if __name__ == '__main__':
    input_url = 'https://www.baidu.com/'

    test_gzip(input_url)
    #print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    # 0.16
    end_time = time.time()
    duration = end_time - start_time
    print duration