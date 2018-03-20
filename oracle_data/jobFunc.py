# coding=utf-8
from __future__ import division
import cx_Oracle
import traceback
import sys
import re
import time
import os
import datetime
import commonTools



#create执行函数，入参均为str，返回值0为成功，其他失败
def executeCreate(logfile,account,password,databaseUrl,needToDrop,tableName,sqlText):

	d_nowdate=datetime.datetime.now()
	s_nowdate=d_nowdate.strftime('%Y%m%d')
	s_yesdate=commonTools.getHisdate(d_nowdate,-1)
        s_startdate=commonTools.getHisdate(d_nowdate,-7)
	s_monthFirstdate=commonTools.getMonthFirstdate()
	s_monthLastdate=commonTools.getMonthLastdate()

	#替换sqlText中的变量

	sqlText=sqlText.replace('$monthFirstdate',s_monthFirstdate)
	sqlText=sqlText.replace('$currentdate',s_nowdate)
	sqlText=sqlText.replace('$yesdate',s_yesdate)
        sqlText=sqlText.replace('$startdate',s_startdate)

	tableChkSql='select 1 from user_tables where table_name = \''+tableName + '\' '
	sqlDrop='drop table '+tableName +' '
	commonTools.printLog(logfile,sqlText)
	commonTools.printLog(logfile,tableChkSql)
	commonTools.printLog(logfile,sqlDrop)
	conn=cx_Oracle.connect(account, password, databaseUrl)
	cursor = conn.cursor()
	
	try:
		cursor.execute(tableChkSql)
		result=cursor.fetchone()
		if result:
			cursor.execute(sqlDrop)
			commonTools.printLog(logfile,tableName +'已存在，删除成功')
		cursor.execute(sqlText)
		return 0
	except:
		traceback.print_exc(file=logfile)
		return -1

#create执行函数，入参均为str，返回值0为成功，其他失败
def needToTruncate(logfile,account,password,databaseUrl,needToTruncate,tableName,sqlText):

	d_nowdate=datetime.datetime.now()
	s_nowdate=d_nowdate.strftime('%Y%m%d')
	s_yesdate=commonTools.getHisdate(d_nowdate,-1)
        s_startdate=commonTools.getHisdate(d_nowdate,-7)
	s_monthFirstdate=commonTools.getMonthFirstdate()
	s_monthLastdate=commonTools.getMonthLastdate()

	#替换sqlText中的变量

	sqlText=sqlText.replace('$monthFirstdate',s_monthFirstdate)
	sqlText=sqlText.replace('$currentdate',s_nowdate)
	sqlText=sqlText.replace('$yesdate',s_yesdate)
        sqlText=sqlText.replace('$startdate',s_startdate)

	tableChkSql='select 1 from user_tables where table_name = \''+tableName+ '\' '
	sqlTruncate='truncate table '+tableName +' '
	commonTools.printLog(logfile,sqlText)
	commonTools.printLog(logfile,tableChkSql)
	commonTools.printLog(logfile,sqlTruncate)
	conn=cx_Oracle.connect(account, password, databaseUrl)
	cursor = conn.cursor()
	
	try:
		cursor.execute(tableChkSql)
		result=cursor.fetchone()
		if result:
			cursor.execute(sqlTruncate)
			commonTools.printLog(logfile,tableName +'已存在，删除成功')
		cursor.execute(sqlText)
		return 0
	except:
		traceback.print_exc(file=logfile)
		return -1
	

#select执行函数，入参均为str，返回值为0为成功，其他为失败，
#执行结果输出到outFile,执行结果只支持输出int和str，不支持date及其他类型，自行在sql中转换好
def executeSelect(logfile,account,password,databaseUrl,sqlText,outFile,sperator):

	d_nowdate=datetime.datetime.now()
	s_nowdate=d_nowdate.strftime('%Y%m%d')
	s_yesdate=commonTools.getHisdate(d_nowdate,-1)
        s_startdate=commonTools.getHisdate(d_nowdate,-7)
	s_monthFirstdate=commonTools.getMonthFirstdate()
	s_monthLastdate=commonTools.getMonthLastdate()
	s_thirdmonthLastdate=commonTools.getThirdMonthFirstdate()
	s_nextmonthLastdate=commonTools.getnextMonthFirstdate()

	#替换sqlText中的变量
	sqlText=sqlText.replace('$monthFirstdate',s_monthFirstdate)
	sqlText=sqlText.replace('$currentdate',s_nowdate)
	sqlText=sqlText.replace('$yesdate',s_yesdate)
        sqlText=sqlText.replace('$startdate',s_startdate)
        sqlText=sqlText.replace('$s_thirdmonthLastdate',s_startdate)
        sqlText=sqlText.replace('$s_nextmonthLastdate',s_startdate)

	commonTools.printLog(logfile,'执行sql：'+sqlText)
	conn=cx_Oracle.connect(account, password, databaseUrl)
	cursor = conn.cursor()
	
	try:
		cursor.execute(sqlText)
		row=cursor.fetchone()
		outFile=outFile.replace('$currentdate',s_nowdate)
		output=open(outFile,'a')
		while row:
			for column in row:
				if type(column)==int:
					output.write(str(column)+sperator)
				elif type(column)==str:
					output.write(column+sperator) 
                                elif type(column)==float:
                                        output.write(str(column)+sperator)

				else:
					commonTools.printLog(logfile,'执行结果存在不支持的变量类型，只支持str和int')
					return -1
			output.write('\n')
			row=cursor.fetchone()
		output.close()
		return 0
	except:
		traceback.print_exc(file=logfile)
		return -1



#insert执行函数，入参均为str，返回值0为成功，其他失败
def executeInsert(logfile,account,password,databaseUrl,tableName,sqlText):

	d_nowdate=datetime.datetime.now()
	s_nowdate=d_nowdate.strftime('%Y%m%d')
	s_yesdate=commonTools.getHisdate(d_nowdate,-1)
        s_startdate=commonTools.getHisdate(d_nowdate,-7)
	s_monthFirstdate=commonTools.getMonthFirstdate()
	s_monthLastdate=commonTools.getMonthLastdate()
	#s_thirdmonthLastdate=commonTools.getThirdMonthFirstdate()
	#s_nextmonthLastdate=commonTools.getnextMonthFirstdate()

	#替换sqlText中的变量

	sqlText=sqlText.replace('$monthFirstdate',s_monthFirstdate)
	sqlText=sqlText.replace('$currentdate',s_nowdate)
	sqlText=sqlText.replace('$yesdate',s_yesdate)
        sqlText=sqlText.replace('$startdate',s_startdate)
       #sqlText=sqlText.replace('$s_thirdmonthLastdate',s_thirdmonthLastdate)
       #sqlText=sqlText.replace('$s_nextmonthLastdate',s_nextmonthLastdate)

	tableChkSql='select 1 from user_tables where table_name = \''+tableName + '\' '
	commonTools.printLog(logfile,sqlText)
	commonTools.printLog(logfile,tableChkSql)
	conn=cx_Oracle.connect(account, password, databaseUrl)
	cursor = conn.cursor()
	
	try:
		cursor.execute(tableChkSql)
		result=cursor.fetchone()
		if result:
			commonTools.printLog(logfile,tableName +'接收表不为空')
		cursor.execute(sqlText)
                conn.commit()
		return 0
	except:
		traceback.print_exc(file=logfile)
		return -1





#insert执行函数，入参均为str，返回值0为成功，其他失败
def executeAlter(logfile,account,password,databaseUrl,tableName,sqlText):


	s_thirdmonthLastdate=commonTools.getThirdMonthFirstdate()
	s_nextmonthLastdate=commonTools.getnextMonthFirstdate()

	#替换sqlText中的变量


        sqlText=sqlText.replace('$s_thirdmonthLastdate',s_thirdmonthLastdate)
        sqlText=sqlText.replace('$s_nextmonthLastdate',s_nextmonthLastdate)

	tableChkSql='select 1 from user_tables where table_name = \''+tableName + '\' '
	commonTools.printLog(logfile,sqlText)
	commonTools.printLog(logfile,tableChkSql)
	conn=cx_Oracle.connect(account, password, databaseUrl)
	cursor = conn.cursor()
	
	try:
		cursor.execute(tableChkSql)
		result=cursor.fetchone()
		if result:
			commonTools.printLog(logfile,tableName +'接收表不为空')
		cursor.execute(sqlText)
                conn.commit()
		return 0
	except:
		traceback.print_exc(file=logfile)
		return -1





