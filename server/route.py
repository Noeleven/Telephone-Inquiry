#!/usr/bin/python
# -*- coding:utf8 -*-

from login import *
from switch import *
from Input import *
from modify import *
from delete import *

route_map={
	
    'login':login,
    'switch':switch,
    'input':Input,
    'modify':modify,
    'delete':delete
}
