#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import json
import time
from urlparse import urlparse

from deepd.aliyun.api.gateway.sdk import client
from deepd.aliyun.api.gateway.sdk.common import constant
from deepd.aliyun.api.gateway.sdk.http import request
from deepd.conf.Config import *
from deepd.security.Pycrypt import Pycrypt


def predict(url, app_key, app_secret, img_base64, kv_config, old_format):
    statTime = time.time()
    cli = client.DefaultClient(app_key=app_key, app_secret=app_secret)
    if not old_format:
        param = {}
        param['image'] = img_base64
        if kv_config is not None:
            param['configure'] = json.dumps(kv_config)
        body = json.dumps(param)
    else:
        param = {}
        pic = {}
        pic['dataType'] = 50
        pic['dataValue'] = img_base64
        param['image'] = pic

        if kv_config is not None:
            conf = {}
            conf['dataType'] = 50
            conf['dataValue'] = json.dumps(kv_config)
            param['configure'] = conf

        inputs = {"inputs": [param]}
        body = json.dumps(inputs)

    url_ele = urlparse(url)
    host = 'http://' + url_ele.hostname
    path = url_ele.path
    headers = {}
    req_post = request.Request(host=host, protocol=constant.HTTP, url=path, headers=headers, method="POST",
                               time_out=6000)
    req_post.set_body(bytearray(source=body, encoding="utf8"))
    req_post.set_content_type(constant.CONTENT_TYPE_STREAM)
    stat, header, content = cli.execute(req_post)
    endTime = time.time()
    print endTime - statTime
    return stat, dict(header) if header is not None else {}, content

class DeepDClient(object):

    def __init__(self):
        cryptor = Pycrypt()
        self.__key = cryptor.decrypt(app_conf['key'])
        self.__secret = cryptor.decrypt(app_conf['secret'])
    #如果输入带有inputs, 设置为True，否则设为False
    def transform(self, imgBase64Str, config, format):
        stat, header, content = predict(app_conf['url'], self.__key, self.__secret, imgBase64Str, config,
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

    def getImgBase64Str(self,img_file):
        with open(img_file, 'rb') as infile:
            s = infile.read()
            return base64.b64encode(s)


