#!/usr/bin/python
# -*- coding:utf8 -*-

import string
from display import *
from operatedb import *
from urllib import unquote

def modify(env, bodysize, input, output):
   
    post_data = input.read(bodysize).split(',')
    msg = {}
    msg['modify_ok'] = 'no'
    Id = post_data[0].split(':')[1]
    name = post_data[1].split(':')[1].split('"')[1]
    mphone = post_data[2].split(':')[1].split('"')[1]
    nphone = post_data[3].split(':')[1].split('"')[1]
    mail = post_data[4].split(':')[1].split('"')[1]
    position = post_data[5].split(':')[1].split('"')[1]
    sql = "select * from Inquiry_DB where flag=1"
    try:
        res = readsql("../config/db.conf",sql)
    except IOError,data:
        print "mysql error:",data
	display(msg,output)
	return
    k = 1
    for row in res:
	if k == string.atoi(Id):
	    sql2="update Inquiry_DB set name='"+name+"',Inum='"+mphone+"', Lnum='"+nphone+"',mailaddr='"+mail+"',position='"+position+"' where name='"+row[1]+"'"
	    try:
	        exesql("../config/db.conf",sql2)
	    except Exception,data:
	        print "mysql error:",sql2
		display(msg,output)
		return
	    msg['modify_ok'] = 'ok'
	    display(msg,output)
	    break
	else:
	    k+=1
	    continue
    else:
        display(msg,output)
