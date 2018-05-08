#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy


class baidu(scrapy.Spider):
    name = 'baidu'
    start_urls = ['https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=怕长', ]

    def parse(self, response):
        yield {
            "biaoti": response.xpath('//div[data-tools]/text()').extract_first()
        }
