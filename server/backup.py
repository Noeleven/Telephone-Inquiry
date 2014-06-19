#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import time

#1.定义原文件
source = ['/rd/test/server/','/rd/test/config/']
#2.定义输出路径
target_dir = '/rd/test/backup/'
today = target_dir + time.strftime('%Y%m%d')
#2.1 检查创建目录
if not os.path.exists(today):
	os.mkdir(today)
	print "成功创建目录",today
#3.定义输出文件名
now = time.strftime('%H%M%S')
input_num = ["1:配置文件","2:程序文件","3:其他"]
print input_num[0]
print input_num[1]
print input_num[2]
print '********************'

remark = raw_input("请选择:")
if remark == "1":
	target_name = today + os.sep + now +'_' + 'config'  '.zip'
elif remark == "2":
	target_name = today + os.sep + now +'_' + 'python'  + '.zip'
else:
	target_name = today + os.sep + now +'.zip'
#4.定义压缩方法
zip_command = "zip -qr '%s' %s" % (target_name,' '.join(source))
print "zip命令是",zip_command
#5.运行程序
if os.system(zip_command) == 0 :
	print "成功备份到",target_name
else:
	print "备份失败"

