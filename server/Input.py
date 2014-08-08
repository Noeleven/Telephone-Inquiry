#!/usr/bin/python
# -*- coding:utf8 -*-

from display import *
from operatedb import *
from urllib import unquote

def Input(env, bodysize, input, output):
    
    post_data = input.read(bodysize).split(',')

    msg = {}
    msg['input_ok'] = 'no'
    name = post_data[0].split(':')[1].split('"')[1]
    mphone = post_data[1].split(':')[1].split('"')[1]
    nphone = post_data[2].split(':')[1].split('"')[1]
    mail = post_data[3].split(':')[1].split('"')[1]
    position = post_data[4].split(':')[1].split('"')[1]
    sql = "select * from Inquiry_DB where flag=1"
    try:
        res = readsql("../config/db.conf",sql)
    except IOError,data:
        print "mysql error:",data
	display(msg,output)
	return
    
    for row in res:
	if row[1] == name:
            msg['input_ok'] = 'being'
	    display(msg,output)
	    break
    else:
            sql2 = "insert into Inquiry_DB(name,Inum,Lnum,mailaddr,position,flag) values('"+name+"','"+mphone+"','"+nphone+"','"+mail+"','"+position+"',1)"
	    try:
	        exesql("../config/db.conf",sql2)
	    except Exception,data:
	        print "mysql error:",data
		display(msg,output)
		return
	    msg['input_ok'] = 'ok'
	    display(msg,output)
