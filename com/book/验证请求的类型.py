#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from lxml import etree

# from bs4 import BeautifulSoup
# session = requests.Session()
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
#             "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
# url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
# req = session.get(url, headers=headers)
# bsObj = BeautifulSoup(req.text)
# print(bsObj.find("table",{"class":"table-striped"}).get_text)

session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', }

url = 'https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending'

req = session.get(url, headers=headers)

result = etree.HTML(req.text)
print(result.xpath('//table[@class="table table-striped"]/tr/*/text()'))
