# -*- coding:utf-8 -*-
from deepd.conf.Config import SECRET_KEY,SALT
import privy

_key = SECRET_KEY
_salt = SALT
class Privakable(object):

    def encrypt(self,plainText):
        return privy.hide(secret=plainText,password=_key,salt=_salt)
    def decrypt(self,secretText):
        return privy.peek(hidden=secretText,password=_key)

# p = Privakable()
# a =  p.encrypt('http://dm-51.data.aliyun.com/rest/160601/ocr/ocr_idcard.json')
# print a
# print p.decrypt(a)