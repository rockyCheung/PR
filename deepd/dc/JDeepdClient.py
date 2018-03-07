# -*- coding: utf-8 -*-

import json
import time
from urlparse import urlparse
from deepd.aliyun.api.gateway.sdk import client
from deepd.aliyun.api.gateway.sdk.common import constant
from deepd.aliyun.api.gateway.sdk.http import request
from deepd.conf.Config import *
import base64

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

def getPRConf():
    return {'prkey':getKey(),'prsecret':getSecret(),'prurl':getUrl()}


def getImgBase64Str(img_file):
    with open(img_file, 'rb') as infile:
        s = infile.read()
        return base64.b64encode(s)