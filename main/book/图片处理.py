#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image, ImageFilter

#清理图片
kitten = Image.open('kitten.jpg')
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save('kitten_blurred.jpg')
blurryKitten.show()
