#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import re

pattern=re.compile(r'([a-z]+) ([a-z]+)',re.I)
m = pattern.match('Hello World Wide Web')
print m
print m.group(0)
print m.span(0)
print m.group(1)
print m.span(1)
print m.group(2)
print m.span(2)
print m.groups()

pattern=re.compile(r'\d+')
k = pattern.match('one12twothree34four',3,10) # 从'1'的位置开始匹配，正好匹配,返回一个 Match 对象
print k.group()
