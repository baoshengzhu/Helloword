#!/usr/bin/env python  
#encoding=utf-8

import paramiko  

#远程服务器  
hostname = ['192.168.132.145']
#端口  
port = 22  
#用户名  
username = 'root'  
#密码  
password = 'benson'  
#执行的命令
#cmd = 'yum install -y vim'
cmd = "free && df -h > /tmp/123321.txt"

#创建SSH连接日志文件（只保留前一次连接的详细日志，以前的日志会自动被覆盖）  
paramiko.util.log_to_file('paramiko.log')

#建立SSH连接  
for ip in hostname: 
	#创建远程连接对象s  
	s = paramiko.SSHClient()  
	#允许连接不在know_hosts文件中的主机
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
	#开始连接	
	s.connect(ip,port,username,password)  
	#远程执行的命令
	stdin,stdout,stderr = s.exec_command(cmd)  
	#打印标准输出  
	print stdout.read()  
	s.close()
