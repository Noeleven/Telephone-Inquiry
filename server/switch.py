#!/usr/bin/python
# -*- coding:utf8 -*-

from operatedb import readsql
from display import *

def switch(env,bodysize,input,output):

    msg = []
    num = 1
    sql = "select * from Inquiry_DB where flag=1"
    try:
        res = readsql("../config/db.conf",sql)
    except Exception,data:
        print "mysql error:",sql
    for row in res:
	
        msg.append({"id":num,"name":row[1],"mphone":row[2],"nphone":row[3],"mail":row[4],"position":row[5]})
	num+=1
    display(msg,output)

