#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from lxml import etree
import re
import sys
import time
import random
import datetime
from main.util.sendemailutil import sendemail
from main.util.mysqlutil import mysqlutil

# sys.path.append(r"D:\workspace\py\main")
# from util.mysqlutil import *


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', }
session = requests.session()


# 得到小说列表页的章节名链接
def getNewUrl(url):
    print(url)
    sleepLitte()
    req = session.get(url, headers=headers)
    req.content.decode(req.encoding, "ignore").encode("utf-8", "ignore")
    result = etree.HTML(req.content)
    return result.xpath('//div[@id="list"]//a/@href')


# 查找最后的存储链接的位置，并返回之后的链接
def cleanNewUrl(urls, saveUrl):
    urls = urls[::-1]
    newUrls = []
    for url in urls:
        if url == saveUrl:
            return newUrls
        else:
            newUrls.insert(0, url)


# 获得小说界面的标题和内容
def getContent(url):
    print(url)
    sleepLitte()
    req = session.get(url, headers=headers)
    req.content.decode(req.encoding, "ignore").encode("utf-8", "ignore")
    result = etree.HTML(req.content)
    return [str(result.xpath('//h1/text()')), str(result.xpath('//div[@id="content"]//text()'))]


# 清理小说界面的文字
def cleanStr(str):
    str = str.replace(r'\r\n', '\r\n    ')
    str = re.sub(r"[\\,rn'xa0\[\]]", '', str)
    return str


# 保存文字到文件
def saveFile(str, name):
    try:
        f = open(name + ".txt", 'w')
        f.write(str)
    except IOError:
        print("%s.txt保存失败", name)
    finally:
        f.close()


def sleepLong():
    time.sleep(random.randint(600, 700))


def sleepLitte():
    time.sleep(random.randint(5, 10))


if __name__ == '__main__':
    mysql = mysqlutil()
    count = 0
    while True:
        count += 1
        session = requests.session()
        print('重复了%s次，当前时间为%s' % (count, datetime.datetime.now()))

        beans = mysql.getUrlBean()
        print(beans)
        for bean in beans:
            url = bean['url']
            newUrls = getNewUrl(url)
            saveUrl = bean['newAddress']
            newUrls = cleanNewUrl(newUrls, saveUrl)
            for needAdress in newUrls:
                titleAndContent = getContent(url + needAdress)
                title = cleanStr(titleAndContent[0])
                content = cleanStr(titleAndContent[1])
                sendemail().send(title, '自己', '自己', content)
                mysql.updataAddress(bean['id'], needAdress)
        session.close()
        sleepLong()
