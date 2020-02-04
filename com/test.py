#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import os
import requests
from PIL import Image
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', }
session = requests.session()

import cv2

if __name__ == '__main__':
    img1 = cv2.imread('./aa.png', cv2.IMREAD_GRAYSCALE)
    # img1 = cv2.resize(img1, (300, 300), interpolation=cv2.INTER_AREA)
    res1 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 5)
    res2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 5)
    cv2.imwrite('11.png', res1)
    cv2.imwrite('12.png', res2)
    # a =Image.open("111111.png")
    # a.show()
    # res1 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,5)
    # res2 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,5)
    #
    # cv2.imshow('res1',res1)
    # cv2.imshow('res2',res2)
