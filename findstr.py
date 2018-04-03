#!/bin/env/python
#coding:utf-8
import os
import re


def findstr(filepath):
    for root,dirname,files in os.walk(filepath):
        for name in files:
            filename=os.path.join(root,name)
                with open(filename)as f:
                    for line in f:
                        if re.findall("package_logger",line):
                            print(filename)
                                break


findstr('/gitpython/health-checker')

