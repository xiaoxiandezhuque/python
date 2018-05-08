#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy
import re
from com.xiaoshuo.xiaoshuo.xiaoshuo.items import XiaoshuoItem


class shuoxiao(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['3qzone.com']

    # start_urls = ['http://pythonscraping.com/pages/cookies/login.html']

    def start_requests(self):
        for bean in self.data:
            yield scrapy.Request(url=bean['url'], callback=self.parse)

    def parse(self, response):

        newUrls = response.xpath('//div[@id="list"]//a/@href').extract()
        for bean in self.data:
            if (bean['url'] == response.url):
                saveUrl = bean['newAddress']
        needUrls = self.cleanNewUrl(newUrls, saveUrl)

        for url in needUrls:
            yield scrapy.Request(url=response.url + url, callback=self.parse_item)

        # 查找最后的存储链接的位置，并返回之后的链接

    def parse_item(self, response):
        item = XiaoshuoItem()
        baseUrl = response.url[0:response.url.rfind('/') + 1]
        for bean in self.data:
            if (bean['url'] == baseUrl):
                item['id'] = bean['id']

        item['title'] = self.cleanStr(str(response.xpath('//h1/text()').extract()))
        item['content'] = self.cleanStr(
            str(response.xpath('//div[@id="content"]//text()').extract()))
        item['newAddress'] = response.url[response.url.rfind('/') + 1:]
        return item

    def cleanNewUrl(self, urls, saveUrl):
        urls = urls[::-1]
        newUrls = []
        for url in urls:
            if url == saveUrl:
                return newUrls
            else:
                newUrls.insert(0, url)
        return newUrls
        # 清理小说界面的文字

    def cleanStr(self, str):
        str = str.replace(r'\r\n', '\r\n    ')
        str = re.sub(r"[\\,rn'xa0\[\]]", '', str)
        return str
