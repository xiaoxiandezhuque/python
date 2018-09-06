#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import subprocess

import sys

from PIL import Image
import pytesseract

# 上面都是导包，只需要下面这一行就能实现图片文字识别
text = pytesseract.image_to_string(Image.open(r'E:\work\python\com\android\1.png'), lang='chi_sim')
print(text)
print(type(text))
if text.__contains__("召 唤"):
    print("true")
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
#
# aaa = "1"
# if aaa == "1":
#     print("====")
