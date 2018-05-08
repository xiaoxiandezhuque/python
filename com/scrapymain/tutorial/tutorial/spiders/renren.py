#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy

from com.scrapymain.tutorial.tutorial.spiders.item.renrenItem import RenrenItem


class renren(scrapy.Spider):
    name = "renren"
    # http://www.renren.com/SysHome.do
    start_urls = [
        'http://www.renren.com/SysHome.do',
    ]

    def start_requests(self):
        return [scrapy.FormRequest('http://www.renren.com/PLogin.do',
                                   formdata={'email': '18180646037', 'password': 'kongzhagen.com'},
                                   callback=self.login)]

    def login(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        item = RenrenItem()
        basicInfo = response.xpath('//div[@id="basicInfo"]')
        name = basicInfo.xpath('').extract_first()
        # sex = basicInfo.xpath('div[2]/dl[1]/dd/text()').extract()[0]
        # birthday = basicInfo.xpath('div[2]/dl[2]/dd/a/text()').extract()
        # birthday = ''.join(birthday)
        # addr = basicInfo.xpath('div[2]/dl[3]/dd/text()').extract()[0]
        #
        # item['sex'] = sex
        # item['addr'] = addr
        # item['birthday'] = birthday
        item['name'] = name
        return item
