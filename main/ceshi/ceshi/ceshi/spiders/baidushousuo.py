#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy


class baidu(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=哈哈']

    # def start_requests(self):
    #     url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=哈哈'
    #     yield scrapy.Request(url=url, callback=self.parse, headers={
    #         'Referer': 'https://baidu.com/',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    #         'Host': 'www.baidu.com'
    #     })

    def parse(self, response):
        self.logger.info('访问', response.url)

        yield {
            "url": response.url,
            "biaoti": response.xpath('//div[@data-tools]/@data-tools').extract_first(),
        }
