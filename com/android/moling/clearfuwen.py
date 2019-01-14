import os

from com.android import findpic
from com.android import adbshell
from com.android.moling import myUtils
import cv2
import numpy as np
from PIL import Image
import time

src_img = r"C:\Users\xh\Nox_share\Image\clear.png"


def takeSecond1(pt):
    return pt[0]


def cleanSet(pointSet, newSet):
    if pointSet:
        point = pointSet.pop()
        newSet.add(point)
        removeSet = set()
        for p in pointSet:
            if abs(point[0] - p[0]) <= 3 and abs(point[1] - p[1]) <= 3:
                removeSet.add(p)
    else:
        return
    pointSet -= removeSet
    cleanSet(pointSet, newSet)


# t = time.time()
# nowTime1 = int(round(t * 1000))
# print(nowTime1 - nowTime);
#
# cv2.imwrite('111111.png', img_rgb)


# a =Image.open("111111.png")
# a.show()
if __name__ == "__main__":

    while True:
        os.system("adb -s 127.0.0.1:62001 shell screencap -p /mnt/shared/Image/%s" % "clear.png")
        allset = set()
        for i in range(1, 7):
            findSet = findpic.getAllLoc(src_img, "./clearfuwen/baohu%s.png" % i)
            if len(findSet) > 0:
                allset = allset | findSet
                break
            findSet = findpic.getAllLoc(src_img, "./clearfuwen/baozou%s.png" % i)
            if len(findSet) > 0:
                allset = allset | findSet
                break
            findSet = findpic.getAllLoc(src_img, "./clearfuwen/shouhu%s.png" % i)
            if len(findSet) > 0:
                allset = allset | findSet
                break
            findSet = findpic.getAllLoc(src_img, "./clearfuwen/jizhong%s.png" % i)
            if len(findSet) > 0:
                allset = allset | findSet
                break
            findSet = findpic.getAllLoc(src_img, "./clearfuwen/fanji%s.png" % i)
            if len(findSet) > 0:
                allset = allset | findSet
                break
            findSet = findpic.getAllLoc(src_img, "./clearfuwen/rennai%s.png" % i)
            if len(findSet) > 0:
                allset = allset | findSet
                break
        if (len(allset) > 0):
            a = allset.pop()
            adbshell.tap(a[0], a[1])
            myUtils.sleepLittle()
            adbshell.tap(myUtils.getRandomNumber(1131, 1247), myUtils.getRandomNumber(296, 326))
            myUtils.sleepLittle()
            adbshell.tap(myUtils.getRandomNumber(456, 581), myUtils.getRandomNumber(405, 453))
            myUtils.sleepLittle()
            adbshell.tap(myUtils.getRandomNumber(456, 581), myUtils.getRandomNumber(405, 453))
            myUtils.sleepLittle()
        else:
            adbshell.swipe(myUtils.getRandomNumber(912, 1175), myUtils.getRandomNumber(550, 661),
                           myUtils.getRandomNumber(912, 1175), myUtils.getRandomNumber(384, 421))
            myUtils.sleepLittle()
            print("滑动找下一页")
    # print(len(allset))
    # if len(allset) != 0:
    #
    #     img_rgb = cv2.imread(src_img)
    #     for pt in allset:
    #         cv2.rectangle(img_rgb, (int(pt[0]), int(pt[1])), (int(pt[0]) + int(10), int(pt[1]) + int(10)), (0, 0, 255),
    #                       2)
    #     cv2.imwrite('111111.png', img_rgb)
    #     a = Image.open("111111.png")
    #     a.show()
    #     newList = list(allset)
    #     newList.sort(key=takeSecond)
    #     print(newList)
    #     # while True:

    pass
