#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # 爬去这些网站
    # def start_requests(self):
    #     urls = ['http://quotes.toscrape.com/page/1/',
    #             'http://quotes.toscrape.com/page/2/', ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    #  上面的代码可以直接写成这样，快捷方式
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    # 写下来
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    # 使用 scrapy crawl quotes -o quotes.json  可以吧趴下来的数据通过json存下来
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        #   对a  有快捷方式 这段和下面的一样
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)

        #    next_page = response.css('li.next a::attr(herf)').extract_first()
        #     if next_page is not None:
        #         #这个是下面两句的简便方式
    #        yield response.follow(next_page,callable=self.parse)
    #       # next_page = response.urljoin(next_page)
    #         # yield scrapy.Request(next_page, callback=self.parse)
