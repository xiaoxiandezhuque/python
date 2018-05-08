#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"D:\Users\Administrator\Desktop\chromedriver.exe")
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())
driver.close()