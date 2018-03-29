#!/bin/env/python
#coding:utf-8
import sys
print(sys.getdefaultencoding())

s="你好"
s_to_unicode=s.decode("utf-8")
print(s_to_unicode,type(s_to_unicode))
s_to_gbk=s_to_unicode.encode("gbk")
print(s_to_gbk)


gbk_to_utf8=s_to_gbk.decode("gbk").encode("utf-8")
print(gbk_to_utf8)
