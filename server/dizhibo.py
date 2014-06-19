#!/usr/bin/python
# -*- coding: utf8 -*-
import cPickle as c
import os

#定义选项内容
option = '''
1.all messages
2.add someone
3.del someone
4.modify someone
5.quit
'''
#todo：
#1.将判断是否增加，删除，修改成功的定义为函数，配以标志位
#2.变量命名改进，避免单字母
#3.避免全局变量

#定义增加人员函数
def add():
	i = len(members)
	a = {}
	if members == []:
		y = 0
	else:
		x = members[-1]
		y = x['uid']
	a['uid'] = y + 1
	a['name'] = raw_input("输入用户名:")
	a['username'] = raw_input("输入姓名:")
	a['email'] = raw_input("输入email:")
	members.append(a)
	f = file(mf,'w')
	c.dump(members,f)
	f.close()
	if len(members) == i + 1:
		print "add success"
	else:
		print "a error!"
	
#定义删除人员函数
def delete():
	i = len(members)
	try:
		x = int(raw_input("输入要删除的人员ID："))
		if x > 0:
			y = 0
			for member in members:
				if x == member['uid']:
					del members[y]
					f = file(mf,'w')
					c.dump(members,f)
					f.close()
				else:
					y += 1
		else:
			print "uid无效"
	except ValueError:
		print "请输入数字"
	
	if len(members) == i - 1:
		print "delete success"
	else:
		print "d error!"
	
#定义修改人员函数
def modify():
	i = len(members)
	while True:
		try:
			x = int(raw_input("输入要修改的人员uid："))
			if x > 0:
				if members == []:
					print "还没有人员信息"
					break
				else:
					y = members[x-1]
					print "name:%s username:%s email:%s" % (y['name'],y['username'],y['email'])
					y['name'] = raw_input("输入用户名:")
					y['username'] = raw_input("输入姓名:")
					y['email'] = raw_input("输入email:")
					members[x-1] = y
					f = file(mf,'w')
					c.dump(members,f)
					f.close()
					if len(members) == i:
						print "m success"
						break
					else:
						print "m error"
			else:
				print "无效uid"
		except ValueError:
			print "请输入数字"

#定义显示所有信息函数
def allMessages():
	for member in members:
		print "uid:%s name:%s username:%s email:%s\n" % (member['uid'],member['name'],member['username'],member['email']),

#检查文件是否存在
def checkfile():
	global mf
	global members
	mf = 'members.data'
	if os.path.exists(mf):
		f = file(mf)
		members = c.load(f)
		f.close()
	else:
		members = []
	message()

#定义交互界面函数
def message():
	while True:
		print "*"*50
		print option
		print "*"*50
		try:
			a = int(raw_input("输入您的选择:"))
			if a == 1:
				print "所有信息：\n"
				allMessages()
			elif a == 2:
				add()
			elif a == 3:
				delete()
			elif a == 4:
				modify()
			elif a == 5:
				break
			else:
				print "这不是一个有效的数字，重新输入吧亲"
		except ValueError:
			print "请输入数字"
	print "Bye！"

if __name__ == "__main__":
	checkfile()
