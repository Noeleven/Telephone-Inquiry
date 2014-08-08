#!/usr/bin/python
# -*- coding:utf8 -*-

from display import *
from operatedb import *
from urllib import unquote

def delete(env, bodysize, input, output):
   
    post_data = {}
    post_data = json.loads(input.read(bodysize))
    msg = {}
    msg['del_ok'] = 'no'
    
    Id = post_data['id']
    sql = "select * from Inquiry_DB where flag=1"
    try:
        res = readsql("../config/db.conf",sql)
    except IOError,data:
        print "mysql error:",data
	display(msg,output)
	return
    k = 1
    for row in res:
	if k == Id:
	    sql2="update Inquiry_DB set flag=0 where name='"+row[1]+"'"
	    try:
	        exesql("../config/db.conf",sql2)
	    except Exception,data:
	        print "mysql error:",sql2
		display(msg,output)
		return
	    msg['del_ok'] = 'ok'
	    display(msg,output)
	    break
	else:
	    k+=1
	    continue
    else:
        display(msg,output)
