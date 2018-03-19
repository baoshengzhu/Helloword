#!/usr/bin/python
#coding:utf-8
import re
 
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I) #这里的?号作用:非贪婪模式
 
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
   print "matchObj.span() : ", matchObj.span()
   print "matchObj.start() : ", matchObj.start()
   print "matchObj.end() : ", matchObj.end()
else:
   print "No match!!"
