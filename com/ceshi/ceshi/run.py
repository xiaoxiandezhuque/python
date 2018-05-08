#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy import cmdline



cmdline.execute("scrapy crawl quotes -o a.json".split())