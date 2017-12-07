#!/usr/bin/env python
# encoding: UTF-8

__author__ = 'lauix'
__version__ = "1.2"

import requests
import json
from http import SGK

'''
blog : https://www.fucksec.com/
'''

def findBreach(name):
    result = SGK().findBreach(str(name))
    return json.dumps(result)


def queryBreachs():
    result = SGK().queryBreachs()
    return json.dumps(result)


def findAccount(account):
    result = SGK().findAccount(str(account))
    return json.dumps(result)