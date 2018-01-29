#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ]
driver = webdriver.Chrome(executable_path=r"D:\Users\Administrator\Desktop\chromedriver.exe",
                             service_args=service_args)
driver.get("http://icanhazip.com")
print(driver.page_source)
driver.close()