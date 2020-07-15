# -*- coding: utf-8 -*-
import base64

def decode_base64(data):
   missing_padding = 4 - len(data) % 4
   if missing_padding:
      data += b'=' * missing_padding
      return base64.decodestring(data)


def py_b64(encode_str):
   for i in range(len(encode_str) % 4):
      encode_str += b'='
   return base64.b64decode(encode_str)