#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 创建新的Selenium driver
import time
from selenium import webdriver
from urllib.request import urlretrieve
import subprocess

print('---------------------------')
driver = webdriver.Chrome(r"D:\Users\Administrator\Desktop\chromedriver.exe")
# 有时我发现PhantomJS查找元素有问题,但是Firefox没有。
# 如果你运行程序的时候出现问题，去掉下面这行注释，
# 用Selenium试试Firefox浏览器：
# driver = webdriver.Firefox()
driver.get(
    "http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(5)
# 单击图书预览按钮

driver.find_element_by_id("imgBlkFront").click()

imageList = set()
# 等待页面加载完成
time.sleep(5)
# 当向右箭头可以点击时，开始翻页
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):

    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    # 获取已加载的新页面（一次可以加载多个页面，但是重复的页面不能加载到集合中）
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)
print(imageList)
driver.quit()
# 用Tesseract处理我们收集的图片URL链接
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())
