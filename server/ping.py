#!/usr/bin/python
# -*- coding: utf8 -*-
import os

#定义输入内容
try:
	begin_ip = int(raw_input("请输入起始地址:"))
	end_ip = int(raw_input("请输入结束地址:"))
except:
	print "请输入数字"

#IP有效性检查
def ip_check():
	while True:
		if begin_ip and end_ip not in range(1,255):
			print "请输入一个1-254之间的数字"
		else:
			if end_ip >= begin_ip:
				return False
			else:
				print "结束ip不能大于起始ip"

#定义ping函数
def ping_detect():
	'''
	检测范围
	'''
	ip_check()
	ip_num = end_ip - begin_ip + 1
	ip_range = range(begin_ip,end_ip+ 1)
	for ip in ip_range:
		ping_cmd = "ping 172.16.17.%d -c 2" % ip
		do_cmd = os.popen(ping_cmd)
		online_num = 0
		if "icmp_req" in do_cmd.read():    
			print "ping %d... 在线" % ip
			online_num += 1
		else:
			print "ping %d... 超时" % ip
	print "测试主机%d,共有%d在线" % (ip_num,online_num)

#主程序
if __name__ == "__main__":
	ping_detect()
