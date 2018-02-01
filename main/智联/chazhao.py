#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

import re
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
    req = requests.get(url, headers=headers, timeout=20)
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
            mysqlutil.addDetailUrls(urlsSet)
            urlsSet.clear()
            sleepLittle()


def getDicJob(html):
    dic_detail = {'title': html.xpath("//h1/text()")[0]}

    position_value = html.xpath(
        "//div[@class='terminalpage-left']/ul[@class='terminal-ul clearfix']/li/strong/text()")
    if (len(position_value) > 5):
        dic_detail['num_of_people'] = position_value[5]
        dic_detail['education'] = position_value[4]
        dic_detail['work_year'] = position_value[3]
        dic_detail['nature'] = position_value[2]
        dic_detail['place'] = position_value[1].replace('-', '')
        money = position_value[0]
        i = money.find(r"\xa")
        if (i > 0):
            dic_detail['money'] = money[0:i]
        else:
            dic_detail['money'] = money
    elif (len(position_value) > 4):
        dic_detail['place'] = ''
        dic_detail['num_of_people'] = position_value[4]
        dic_detail['education'] = position_value[3]
        dic_detail['work_year'] = position_value[2]
        dic_detail['nature'] = position_value[1]
        money = position_value[0]
        i = money.find(r"\xa")
        if (i > 0):
            dic_detail['money'] = money[0:i]
        else:
            dic_detail['money'] = money

    state = html.xpath(
        "//div[@class='terminalpage-left']/ul[@class='terminal-ul clearfix']/li/strong/span/text()")
    if (len(state) > 0):
        dic_detail['state'] = state[0]
    else:
        dic_detail['state'] = ''

    category = html.xpath(
        "//div[@class='terminalpage-left']/ul[@class='terminal-ul clearfix']/li/strong/a/text()")
    if len(category) > 1:
        dic_detail['category'] = category[1]
    elif len(category) > 0:
        dic_detail['category'] = category[0]
    else:
        dic_detail['category'] = ''

    tab_inner_cont = html.xpath("//div[@class='tab-inner-cont']")
    if len(tab_inner_cont) < 2:
        return

    address = tab_inner_cont[0].xpath("//h2/text()")
    if (len(address) > 0):
        dic_detail['address'] = re.sub(r"[\r\n ]", '', address[0])
    else:
        dic_detail['address'] = ''

    dic_detail['description'] = str(tab_inner_cont[0].xpath("p/text()")).replace("\"", '')

    company_name = tab_inner_cont[1].xpath("h5/a/text()")
    if len(company_name) > 0:
        dic_detail['company_name'] = company_name[0]
    else:
        dic_detail['company_name'] = ''
    dic_detail['company_detail'] = str(tab_inner_cont[1].xpath("p/text()")).replace("\"", '')
    dic_detail['zl_id'] = dic_url['url_id']

    company_detail = html.xpath("//div[@class='company-box']//li")
    if len(company_detail) > 2:
        company_people = company_detail[0].xpath('strong/text()')
        if len(company_people) > 0:
            dic_detail['company_people'] = company_people[0]
        else:
            dic_detail['company_people'] = ''
        company_nature = company_detail[1].xpath('strong/text()')
        if len(company_nature) > 0:
            dic_detail['company_nature'] = company_nature[0]
        else:
            dic_detail['company_nature'] = ''
        company_industry = company_detail[2].xpath('strong/a/text()')
        if len(company_industry) > 0:
            dic_detail['company_industry'] = company_industry[0]
        else:
            dic_detail['company_industry'] = ''

    return dic_detail


def cleanStr(str):
    return re.sub(r"[\[\]\\rn]", '', str)


def sleepLittle():
    time.sleep(random.randint(3, 4))


if __name__ == "__main__":
    lookUp()
    count = 0
    while (True):
        dic_urls = mysqlutil.getDetailUrls(count, count + 10)
        count += 10
        for dic_url in dic_urls:
            html = getHtml(dic_url['url'])
            dic_detail = getDicJob(html)
            print(dic_detail)
            sleepLittle()
            if (dic_detail is None):
                continue
            else:
                mysqlutil.saveDetail(dic_detail)
