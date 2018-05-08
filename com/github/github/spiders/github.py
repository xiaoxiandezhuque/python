#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy


class github(scrapy.Spider):
    name = 'github'

    def start_requests(self):
        yield scrapy.Request('https://github.com/login')

    def parse(self, response):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': response.xpath('//div/input[2]/@value').extract_first(),
            'login': "962139864@qq.com",
            'password': "542097532qq"
        }

        # yield scrapy.FormRequest('https://github.com/session', formdata=post_data)
        print('-------------------------------------------------')
        print(response.xpath('//h1/text()').extract_first())
        pass

    def parse_session(self, response):
        pass

    def get_param(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        field_one = selector.xpath('//div/input[2]/@value')
        print(field_one)
        return field_one
        pass
