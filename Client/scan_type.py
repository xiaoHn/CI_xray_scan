# -*- coding: utf-8 -*-
import sys

def scan_type():
    try:
        data_type = sys.argv[2]
        return data_type
    except:
        exit('python scanner.py scan_venv scan_type')