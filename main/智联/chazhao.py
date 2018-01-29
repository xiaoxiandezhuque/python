#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import requests
from lxml import etree

base_url = r"http://sou.zhaopin.com/jobs/searchresult.ashx?jl=成都&kw=android&sm=0&p=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', }


# 运行js需要的
def lookHtmlForJs(url):
    chrome_executable_path = r"D:\Users\Administrator\Desktop\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_executable_path)

    driver.get(base_url)
    time.sleep(10)


def getHtml(url):
    req = requests.get(url, headers=headers)
    return etree.HTML(req.text)


def getNextUrl(html):
    html.xpath("")
