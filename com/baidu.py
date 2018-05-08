#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from lxml import etree

try:
    import cookielib
except:
    import http.cookiejar as cookielib


class Baidu(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'www.baidu.com'
        }
        self.sousuo_url = 'https://www.baidu.com/s?wd=哈哈'
        self.session = requests.session()
        self.session.cookies = cookielib.LWPCookieJar(filename='github_cookie')

    def begin(self):
        response = self.session.get(url=self.sousuo_url, headers=self.headers)
        selector = etree.HTML(response.text)
        first_text = selector.xpath('//div[@data-tools]/@data-tools')

        print(first_text)


if __name__ == "__main__":
    Baidu = Baidu()
    Baidu.begin()
