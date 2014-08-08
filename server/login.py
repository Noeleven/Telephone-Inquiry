#!/usr/bin/python
# -*- coding -*-

import json
'''import socket
import fcntl
import struct'''
import urllib2,httplib
from BeautifulSoup import BeautifulSoup
from operatedb import *
from display import *

def login(env,bodysize,input,output):
    
    msg = {}
    msg['ip'] = get_ip()
    display(msg,output)
def get_ip():
    url = 'http://www.ip.cn'
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    ip = soup.find('div',{'class':'well'}).code.text
    return ip

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
	0x8915,  # SIOCGIFADDR
	struct.pack('256s', ifname[:15])
    )[20:24])

	
    
