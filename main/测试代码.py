#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import subprocess

import sys

from PIL import Image
import pytesseract

# 上面都是导包，只需要下面这一行就能实现图片文字识别
text = pytesseract.image_to_string(Image.open(r'E:\work\python\main\android\1.png'), lang='chi_sim')
print(text)
