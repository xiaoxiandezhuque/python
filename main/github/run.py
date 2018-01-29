#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy import cmdline

cmdline.execute("scrapy crawl github".split())

# import os
# import time
#
# while (True):
#     command3 = 'scrapy crawl xiaoshuo'
#     os.system(command3)
#     print("--------------")
#     time.sleep(600)

#  -s LOG_FILE=xx.log  打印日志到文件
