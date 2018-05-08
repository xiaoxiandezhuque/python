#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image, ImageFilter

#清理图片
kitten = Image.open('1.png')
kitten.show()
# blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
# blurryKitten.save('kitten_blurred.png')
# blurryKitten.show()
