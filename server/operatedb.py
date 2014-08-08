#!/usr/bin/env python
# -- coding:utf-8 --
import MySQLdb
import string

def connect(str):

  fo=open(str, "r")
  dbstr=fo.read(70)
  db_list=dbstr.split("=")
  dbhost=db_list[1].split('\n')[0]
  dbport=string.atoi(db_list[2].split('\n')[0])  #从数据库中读取的数据都是字符串，端口是需要数字的，所以进行了转换
  dbuser=db_list[3].split('\n')[0]
  dbpasswd=db_list[4].split('\n')[0]
  dbdb=db_list[5].split('\n')[0]
  return(MySQLdb.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbdb))

def exesql(content,sqlstr):    #直接操作sql语句,content是数据库的配置文件目录
   db=connect(content)
   cursor=db.cursor()
   cursor.execute("set NAMES UTF8")
   cursor.execute(sqlstr)
   db.commit()
   cursor.close()
   db.close()
 
def readsql(content,sqlstr):   #查找数据库的所有数据
    db=connect(content)
    cursor=db.cursor()
    cursor.execute("set NAMES UTF8")
    cursor.execute(sqlstr)
    temp=cursor.fetchall()
    cursor.close()
    db.close()
    return temp
  
