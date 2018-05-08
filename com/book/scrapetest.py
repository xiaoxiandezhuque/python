#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
from urllib.request import urlopen

import re
from bs4 import BeautifulSoup  # 解析html库
from lxml import etree  # 解析html库  使用的xpath

# html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
# # bsObj = BeautifulSoup(html.read())
# result = etree.HTML(html.read())
# print(result.xpath('//div[@id="bodyContent"]//a[starts-with(@href,"/wiki/")]/@href'))

i = 0
pages = set()


def getLinks(articleUrl):
    global pages
    toUrl = "https://en.wikipedia.org" + articleUrl
    html = urlopen(toUrl)
    result = etree.HTML(html.read())
    urls = result.xpath('//div[@id="bodyContent"]//a[starts-with(@href,"/wiki/")]/@href')
    for url in urls:
        if url not in pages:
            pages.add(url)
            getLinks(url)


links = getLinks("/wiki/Kevin_Bacon")
while (len(links) > 0):
    i = i + 1
    newArticle = links[random.randint(0, len(links) - 1)]
    print(newArticle)
    links = getLinks(newArticle)
    if (i > 10):
        break
