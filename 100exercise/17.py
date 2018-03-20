#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import string
s = raw_input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0

for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others)


import re
str=raw_input('请输入一串字符：')
r1=re.compile(r'[a-zA-Z]')
r2=re.compile(r'\d')
r3=re.compile(r'\s')

print '英文字母的个数为: %d' %len(re.findall(r1,str))
print '数字的个数为： %d' %len(re.findall(r2,str))
print '空格的个数为： %d' %len(re.findall(r3,str))
print '其他字符的个数为： %d' %(len(str)-len(re.findall(r1,str))-len(re.findall(r2,str))-len(re.findall(r3,str)))
