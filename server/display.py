#!/usr/bin/python
# -*- coding:utf8 -*-

import json
from content import *

def display(msg,output):

    output.write(CONTENT_TYPE_HEAD)
    output.write(json.dumps(msg))
