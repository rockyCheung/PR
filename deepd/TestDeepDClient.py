#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .conf.Config import *
from .dc.deepd_client import DeepDClient
from .dc.JDeepdClient import getImgBase64Str
import unittest
import json

class TestDeepDClient(unittest.TestCase):
    def testTransform(self):
        img_file = DATA_DIR + '/test.png'
        # 如果输入带有inputs, 设置为True，否则设为False
        is_old_format = True
        config = {'side': 'face'}
        # 如果没有configure字段，config设为None
        # config = None
        ddc = DeepDClient()
        img_base64data = getImgBase64Str(img_file)
        response = ddc.transform(img_base64data, config, is_old_format)
        response = json.loads((response))
        print img_file
        print response
        self.assertEqual(True,response['success'])

if __name__ == '__main__':
    unittest.main()