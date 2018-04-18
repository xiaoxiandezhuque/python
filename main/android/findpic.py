import random

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract


# 模糊匹配，怎么都可以匹配出来
def look(srcimg, findimg):
    img = cv.imread(srcimg, 0)
    img2 = img.copy()
    template = cv.imread(findimg, 0)
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
               'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(img, template, method)
        # loc = np.where( res >= 0.8)
        # print(loc)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img, top_left, bottom_right, 255, 2)
        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show()


# 模糊匹配，找到第一个匹配的点   用这个，有可能会失败
def getLoc(srcimg, findimg):
    img_rgb = cv.imread(srcimg)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread(findimg, 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        # cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        return (random.randrange(pt[0], pt[0] + w), random.randrange(pt[1], pt[1] + h))
    # cv.imwrite('res.png', img_rgb)


def getWord(path):
    # 上面都是导包，只需要下面这一行就能实现图片文字识别
    text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
    print(text)


if __name__ == "__main__":
    a = getLoc("1.png", "wx.png")
    if a:
        print(getLoc("1.png", "wx.png"))
    else:
        print("没找到")
