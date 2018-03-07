#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
__all__ = [
    'BASE_DIR',
    'DATA_DIR',
    'getKey',
    'getSecret',
    'getUrl'
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = BASE_DIR + '/data'

app_conf = {
    'key':'9HrMrxbRHctNP0QhhHEe0lsPo//+E3INGcDGKxbG78gL+vlXkGBH9VER6fa+86FA',
    'secret':'azktEAjubdJmnaq1mJCP+fmj2ijdNW0hGcbZ0PpRXPJZRvAEMbyQ7r8bm6FLyuAArn75eqLWL2xLvdWh46o8gg==',
    'url':'Myvve9L/eNX7uheCkWqVLXGbKv3DI1a0jo7uEyxe22UDsoozXtjuD3fK8q47yQeH0aGcLpIYitEqOBKUfpJz3rxz4TtXXf6GRLz/1full0nRUeceotdI1ELKVANvPPUp'
}

SECRET_KEY = 'sd2dn@ssc$fs16s='
SALT = 'papaasdasdqwdqweqweqwes'

def getKey():
    return app_conf['key']
def getSecret():
    return app_conf['secret']
def getUrl():
    return app_conf['url']