#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import scgi
import scgi.scgi_server

from route import *

reload(sys)
sys.setdefaultencoding('utf-8')

class TimeHandler(scgi.scgi_server.SCGIHandler):
   
   def produce(self, env, bodysize, input, output) :
        
       entrance = env['REQUEST_URI'].split('?')[0].split('/')[2]
       if entrance in route_map:
           route_map[entrance](env,bodysize,input,output)

if __name__ == '__main__' :
    server = scgi.scgi_server.SCGIServer(
        handler_class=TimeHandler,
	host="127.0.0.1",
        port=3010
    )
    server.serve()


