#!/usr/bin/env python
# encoding: UTF-8
import requests


class SGK(object):
    '''
    API : https://haveibeenpwned.com/api/v2/
    '''

    def __init__(self):
        self.url = 'https://haveibeenpwned.com/api/v2/'

    def findBreach(self, name):
        r = requests.get(self.url + 'breach/' + str(name))
        if r.text:
            result = {}
            result['result'] = 'True'
            result['list'] = r.json()
            return result
        else:
            result = {}
            result['result'] = 'False'
            result['list'] = ''
            return result

    def queryBreachs(self):
        r = requests.get(self.url + 'breaches')
        if r.text:
            result = {}
            result['result'] = 'True'
            result['list'] = r.json()
            return result
        else:
            result = {}
            result['result'] = 'False'
            result['list'] = ''
            return result

    def findAccount(self, account):
        r = requests.get(self.url + 'breachedaccount/' + str(account))
        if r.text:
            result = {}
            result['result'] = 'True'
            result['list'] = r.json()
            return result
        else:
            result = {}
            result['result'] = 'False'
            result['list'] = ''
            return result
