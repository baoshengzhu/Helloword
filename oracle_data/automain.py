# coding=utf-8
from __future__ import division
import cx_Oracle
import traceback
import sys
import re
import time
import os
import datetime
import ConfigParser
import jobFunc
import commonTools

homedir='/data/feinno/mwn/tmp'  # 定义主要文件路径
logfile=open(homedir+'/run.log','a') # 调用日志文件
job=sys.argv[1]                      # 定义脚本参数提取
configFile=homedir +'/general.ini'   # 配置文件位置

config = ConfigParser.ConfigParser() # 获取配置文件
config.readfp(open(configFile,"rb")) 

account=config.get(job,"account")    # 账号
password=config.get(job,"password")  # 密码
databaseUrl=config.get(job,"databaseUrl") # 链接
jobtype=config.get(job,"jobtype")  
needToTruncate=config.get(job,"needToTruncate")
needToDrop=config.get(job,"needToDrop")
tableName=config.get(job,"tableName")
sqlFile=config.get(job,"sqlFile")
cycle=config.get(job,"cycle")

sqlFile=open(homedir+'/'+sqlFile,'r') # 读取sql文件
sqlText=sqlFile.read()

commonTools.printLog(logfile,'配置文件读取成功，开始运行'+job+'任务')  # 调用自定义模块commontools


if jobtype=='CREATE':
	rs=jobFunc.executeCreate(logfile,account,password,databaseUrl,needToDrop,tableName,sqlText)
	if rs==0:
		commonTools.printLog(logfile,'job:'+job +'执行成功')
		exit(0)
	else:
		commonTools.printLog(logfile,'job:'+job +'执行失败')
		exit(-1)


if jobtype=='TRUNCATE':
	rs=jobFunc.needToTruncate(logfile,account,password,databaseUrl,needToTruncate,tableName,sqlText)
	if rs==0:
		commonTools.printLog(logfile,'job:'+job +'执行成功')
		exit(0)
	else:
		commonTools.printLog(logfile,'job:'+job +'执行失败')
		exit(-1)


	
if jobtype=='SELECT':
	outFile=config.get(job,"outFile")
	outFile=homedir+'/'+outFile
	sperator=config.get(job,"sperator")
	rs=jobFunc.executeSelect(logfile,account,password,databaseUrl,sqlText,outFile,sperator)
	if rs==0:
		commonTools.printLog(logfile,'job:'+job +'执行成功')
		exit(0)
	else:
		commonTools.printLog(logfile,'job:'+job +'执行失败')

		exit(-1)



if jobtype=='INSERT':
	rs=jobFunc.executeInsert(logfile,account,password,databaseUrl,tableName,sqlText)
	if rs==0:
		commonTools.printLog(logfile,'job:'+job +'执行成功')
		exit(0)
	else:
		commonTools.printLog(logfile,'job:'+job +'执行失败')
		exit(-1)



if jobtype=='ALTER':
	rs=jobFunc.executeAlter(logfile,account,password,databaseUrl,tableName,sqlText)
	if rs==0:
		commonTools.printLog(logfile,'job:'+job +'执行成功')
		exit(0)
	else:
		commonTools.printLog(logfile,'job:'+job +'执行失败')
		exit(-1)

	
logfile.close()


