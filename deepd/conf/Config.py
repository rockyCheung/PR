#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
__all__ = [
    'BASE_DIR',
    'DATA_DIR',
    'getKey',
    'getSecret',
    'getUrl',
    'getPKey',
    'getPSecret',
    'getPUrl'
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = BASE_DIR + '/data'

app_conf = {
    'key':'9HrMrxbRHctNP0QhhHEe0lsPo//+E3INGcDGKxbG78gL+vlXkGBH9VER6fa+86FA',
    'secret':'azktEAjubdJmnaq1mJCP+fmj2ijdNW0hGcbZ0PpRXPJZRvAEMbyQ7r8bm6FLyuAArn75eqLWL2xLvdWh46o8gg==',
    'url':'Myvve9L/eNX7uheCkWqVLXGbKv3DI1a0jo7uEyxe22UDsoozXtjuD3fK8q47yQeH0aGcLpIYitEqOBKUfpJz3rxz4TtXXf6GRLz/1full0nRUeceotdI1ELKVANvPPUp',
    'pkey':'1$2$cGFwYWFzZGFzZHF3ZHF3ZXF3ZXF3ZXM=$Z0FBQUFBQmFuMEJzRFFhZU1MdEpOTEE0ZTJmUjA5OWRKYkg1MXh1N2x4QmhQQXNIZzM5c25XbWVpVkROQjFvRkFQd09GTGowWjhKX0VmZlJ1dTg5QV9XZXhmejkzWXNnUFE9PQ==',
    'psecret':'1$2$cGFwYWFzZGFzZHF3ZHF3ZXF3ZXF3ZXM=$Z0FBQUFBQmFuMEJzNm9QS1NXeVdjSVF3OUZvdmxieEZQb0RjVkZOTEZfdE44LVhGaU1fWlBEWWY4azBFVHhGQmpYQXlJei02ZDNUcG94ZjItbWFKUWJpZWVnNFIyb2NPYm9LY2ZWa1ZlVF9ZUlI2dTh0dEphTmw2UmtZU0x2MzVFVWdMbE91Wm5CcXE=',
    'purl':'1$2$cGFwYWFzZGFzZHF3ZHF3ZXF3ZXF3ZXM=$Z0FBQUFBQmFuMEJzeWNqTWowaWlKWGNKZk82S05ldXBXNFJRYjIxTFczZnAxbm1aN3ZuUWsyTnMxQVk4Z0dDdmM3XzlHU1RqdnRLOTVLSkoyMEJ2YlRvTHptZjhuYlpYeGt0eG12QU1QTkR6VHplaFI3b3pGZUFxZlEyaDdmVUJmc194bC1NcTllNDBha3FxWDgxR3FNWG52ZEp1MThPV2p3PT0='
}

SECRET_KEY = 'sd2dn@ssc$fs16s='
SALT = 'papaasdasdqwdqweqweqwes'

def getKey():
    return app_conf['key']
def getSecret():
    return app_conf['secret']
def getUrl():
    return app_conf['url']
def getPKey():
    return app_conf['pkey']
def getPSecret():
    return app_conf['psecret']
def getPUrl():
    return app_conf['purl']