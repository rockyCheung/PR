# -*- coding:utf-8 -*-
from Crypto.Cipher import AES
import base64
from deepd.conf.Config import SECRET_KEY,SALT

class Pycrypt(object):
    def __init__(self):
        self.key = SECRET_KEY
        self.mode = AES.MODE_CBC
        self.salt = SALT

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        text = text+'@'+self.salt
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        # return b2a_hex(self.ciphertext)
        return base64.encodestring(ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plainText = cryptor.decrypt(base64.decodestring(text))
        plainText = plainText.rstrip('\0')
        return plainText.partition('@')[0]

# from deepd.conf.Config import *
# import privy
# # from AES import AES as aa
# p = Pycrypt()
# # aes = aa()
# print p.decrypt(getKey())
# print p.decrypt(getSecret())#24810465 #069121ead09b645dcf8f7a0b9f355439
# hidden = privy.hide(b'24810465', SECRET_KEY)
# print hidden
# print privy.peek(hidden, SECRET_KEY)
# print aes.encrypt(bytes('24810465'))
# print aes.decrypt(getSecret())