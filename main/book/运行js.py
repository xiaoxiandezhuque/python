#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_executable_path = r"D:\Users\Administrator\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_executable_path)


# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# try:
#     # 等待js执行完毕，出现新的html
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.ID, 'loadedButton'))
#     )
# finally:
#     print(driver.find_element_by_id('content').text)
#     driver.close()


# time.sleep(3)
# print(driver.page_source)
# print('-------')
# print(driver.find_element_by_id('content').text)
# driver.close()

# 客户端重定向，一直搜索一个东西，
def waitForLoad(driver):
    elem = driver.find_element_by_tag_name('html')
    count = 0
    while True:
        count += 1
        if count > 20:
            print('Timing out after 10 seconds and returning')
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name('html')
        except StaleElementReferenceException:
            print("不一样")
            return


driver.get("https://dl.reg.163.com/ydzj/maildl?product=mail163&pdconf=yddl_mail163_conf&mc=0F6099&curl=https%3A%2F%2Fmail.163.com%2Fentry%2Fcgi%2Fntesdoor%3Ffrom%3Dsmart%26language%3D0%26style%3D11%26allssl%3Dfalse%26destip%3D192.168.193.48%26df%3Dsmart_android")
time.sleep(10)
# waitForLoad(driver)
# print(driver.page_source)
# driver.close()