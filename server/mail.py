#!/usr/bin/python
# -*- coding: utf8 -*-

from smtplib import SMTP as smtp
from email.mime.text import MIMEText

mailto_list = ['305820049@qq.com','crazy--qq@163.com']

mail_host = 'smtp.ym.163.com'
mail_user = 'zhangqiang'
mail_pass = '851206sqq'
mail_postfix = 'iceflow.cn'
mail_sub = "测试html格式发送"
mail_msg = ""
for line in open('mail.context'):
	mail_msg += line

def send_mail(to_list,sub,content):
	'''
	to_list 发给谁
	sub 主题
	context 发送内容
	send_mail('to_list','sub','content')
	'''
	mail_from = mail_user+ "<"+ mail_user+ "@"+ mail_postfix+ ">"
	msg = MIMEText(content, _subtype='html', _charset='utf8')
	msg['From'] = mail_from
	msg['To'] = ";".join(mailto_list)
	msg['Subject'] = mail_sub
	try:
		server = smtp(mail_host)
#		server.connect(mail_host)
		server.login(mail_user+ '@'+ mail_postfix,mail_pass)
		server.sendmail(mail_from,mailto_list,msg.as_string())
		server.quit()
		return True
	except Exception,e:
		print str(e)
		return False

if __name__ == "__main__":
	if send_mail(mailto_list,mail_sub,mail_msg):
		print "success"
	else:
		print "failed"
