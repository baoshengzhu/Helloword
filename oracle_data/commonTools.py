# coding=utf-8
from __future__ import division
import cx_Oracle
import traceback
import sys
import re
import time
import os
import datetime

##获取当天日期
def getdate():
	return datetime.datetime.now().strftime('%Y%m%d')

##字符转换日期
def charToDate(str):
	return datetime.datetime.strptime(str,'%Y%m%d').date()

##获得n天后的日期，入参数d为date类型，返回char类型
def getHisdate(d,n):
	hisDate = d + datetime.timedelta(days=n)
	hisDateStr = hisDate.strftime('%Y%m%d')
	return hisDateStr

##获得前一天所在月的第一天日期
def getMonthFirstdate():
	nowTime = datetime.datetime.now()
	yesDate = nowTime + datetime.timedelta(days=-1)
	year = int(yesDate.strftime('%Y'))
	month = int(yesDate.strftime('%m'))
	monthFirstdate=(datetime.datetime(year, month, 1)).strftime("%Y%m%d")
	return monthFirstdate

##获得前一天所在月的最后一天日期
def getMonthLastdate():
	nowTime = datetime.datetime.now()
	yesDate = nowTime + datetime.timedelta(days=-1)
	year = int(yesDate.strftime('%Y'))
	month = int(yesDate.strftime('%m'))
	if 12==month:
		monthLastdate=(datetime.datetime(year, month, 31)).strftime("%Y%m%d")
	else:
		monthLastdate=(datetime.datetime(year, month+1, 1) + datetime.timedelta(days = -1)).strftime("%Y%m%d")
	return monthLastdate


##获得前一天所在月第三月的第一天日期
def getThirdMonthFirstdate():
	nowTime = datetime.datetime.now()
	yesDate = nowTime + datetime.timedelta(days=-1)
	year = int(yesDate.strftime('%Y'))
	month = int(yesDate.strftime('%m'))
	thirdmonthFirstdate=(datetime.datetime(year, month+2, 1)).strftime("%Y-%m-%d %H:%M:%S")
	return thirdmonthFirstdate

##获得前一天所在月第二月的第一天日期
def getnextMonthFirstdate():
	nowTime = datetime.datetime.now()
	yesDate = nowTime + datetime.timedelta(days=-1)
	year = int(yesDate.strftime('%Y'))
	month = int(yesDate.strftime('%m'))
	nextmonthFirstdate=(datetime.datetime(year, month+1)).strftime("%Y%m")
	return nextmonthFirstdate




##写入日志，入参为句柄和str
def printLog(logfile,str):
	currentTime= time.strftime( '%Y-%m-%d %X', time.localtime() )
	logfile.write(currentTime + ' -- ' + str + '\n')

