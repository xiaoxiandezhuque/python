#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import subprocess
import datetime
import time

import sys

from PIL import Image
import pytesseract


now = time.time()

now1 =  time.time()+1000
print(now)
print(now1-now)



# 上面都是导包，只需要下面这一行就能实现图片文字识别
# text = pytesseract.image_to_data(Image.open(r'E:\work\python\main\android\1.png'), lang='chi_sim')
# print(text)
# print(type(text))
# a = text.split("	")
# print("-----------")
# for i in range(0, len(a)):
#     # print(a[i])
#     if "密" in a[i]:
#         print(a[i - 5])
#         print(a[i - 4])
#         print(a[i - 3])
#         print(a[i - 2])
#         break
# print("-----------")
# # print(a)
# # for text1  in a:
# #     print(text1)
# #     print("-------------------")
# aaa = "1"
# if aaa == "1":
#     print("====")

