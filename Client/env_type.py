# -*- coding: utf-8 -*-
import sys

def scan_type_2(scan_env):
    try:
        data_type = sys.argv[2]
        return data_type
    except:
        put_line = "\033[36m[INFO]\033[0m python scanner.py " + scan_env + " scan_type"
        exit(put_line)

def env_type():
    try:
        scan_env = sys.argv[1]
        if 'test' == scan_env:
            env_id = '1'
            scan_type_2(scan_env)
            return env_id

        elif 'yf' == scan_env:
            env_id = '2'
            scan_type_2(scan_env)
            return env_id

        elif 'proc' == scan_env:
            env_id = '3'
            scan_type_2(scan_env)
            return env_id

        else:
            exit("\033[36m[INFO]\033[0m Please enter the correct env type：test|yf|proc")
    except IndexError:
        exit("\033[36m[INFO]\033[0m Please enter the correct line：python scanner.py test beauty......")


def env_host(scan_env):
   if scan_env == '1':
      req_host = 'reqhost_test'
      return req_host
   elif scan_env == '2':
      req_host = 'reqhost_yf'
      return req_host
   elif scan_env == '3':
      req_host = 'reqhost_yf'
      return req_host
   else:
      pass