#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepd.dc.JDeepdClient import *
from deepd.security.Privakable import Privakable

class DeepDClient(object):
    def __init__(self):
        cryptor = Privakable()
        self.__key = cryptor.decrypt(getPKey())
        self.__secret = cryptor.decrypt(getPSecret())
        self.__url = cryptor.decrypt(getPUrl())
    #如果输入带有inputs, 设置为True，否则设为False
    def transform(self, imgBase64Str, config, format):
        stat, header, content = predict(self.__url, self.__key, self.__secret, imgBase64Str, config,
                                        format)
        if stat != 200:
            print 'Http status code: ', stat
            print 'Error msg in header: ', header['x-ca-error-message'] if 'x-ca-error-message' in header else ''
            print 'Error msg in body: ', content
            exit()
        if format:
            result_str = json.loads(content)['outputs'][0]['outputValue']['dataValue']
        else:
            result_str = content

        return result_str


