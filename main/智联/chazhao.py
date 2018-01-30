#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

from selenium import webdriver
import time
import requests
from lxml import etree
import urllib.request

import mysqlutil

base_url = r"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=成都&kw=android&sm=0&p=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', }


# detailUrls = set()


# 运行js需要的
def lookHtmlForJs(url):
    chrome_executable_path = r"D:\Users\Administrator\Desktop\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_executable_path)

    driver.get(base_url)
    time.sleep(10)


def getHtml(url):
    req = requests.get(url, headers=headers)
    html = etree.HTML(req.text)
    req.close()
    return html


def getNextUrl(html):
    #
    return html.xpath("//div//a[@class='next-page']/@href")


def getDetailUrls(html):
    # global detailUrls
    return set(html.xpath("//table/tr/td/div/a/@href"))

    # pass


def lookUp():
    global urlsSet
    urlsSet = set()
    nextUrl = base_url
    while True:
        if (nextUrl):
            print(nextUrl)
            html = getHtml(nextUrl)
            urls = getNextUrl(html)
            if len(urls) > 0:
                nextUrl = urls[0]
            else:
                nextUrl = None
            urls = getDetailUrls(html)
            urlsSet = urlsSet | set(urls)

            time.sleep(random.randint(1, 2))
        else:
            mysqlutil.addDetailUrls(urlsSet)

            break


if __name__ == "__main__":
    # lookUp()
    count = 0
    dic_urls = mysqlutil.getDetailUrls(count, count + 10)
    for url in dic_urls:
        html = getHtml(url)

