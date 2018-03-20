#!/bin/env/python
#coding:utf-8

input = int(raw_input("请输入要分解的正整数:"))

temp = []
while input!=1:
    for i in range(2,input+1):
        if input%i == 0:
            temp.append(i)
            input = input/i
            break
print temp
