import os
import threading
import time
from com.android import findpic
from com.android import adbshell


def saveScreenshot(name):
    os.system("adb  shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb pull /sdcard/%s E:\work\python\com\android\xiaozhuo\img" % name)  # 导出图片
    # os.system(r"adb -s 127.0.0.1:62001 pull /sdcard/%s %s\img" % (name, os.getcwd()))  # 导出图片


src_img = r"E:\work\python\com\android\xiaozhuo\img\11.png"
find_src = r"E:\work\python\com\android\xiaozhuo\img"
state = 0

if __name__ == "__main__":
    # saveScreenshot("11.png")
    while (True):
        saveScreenshot("11.png")

        if (state == 0):
            point = findpic.getLoc(src_img, find_src + r"\dakaishiwan.png")
            if point:
                adbshell.tap(point)
                print("点击试玩")

            point = findpic.getLoc(src_img, find_src + r"\quguanzhu.png")
            if point:
                adbshell.tap(point)
                print("点击去关注")
                state = 1


        elif (state == 1):
            point = findpic.getLoc(src_img, find_src + r"\baocunerweima.png")
            if point:
                adbshell.tap(point)
                print("保存二维码")
                state = 2

        elif (state == 2):
            point = findpic.getLoc(src_img, find_src + r"\tianjia.png")
            if point:
                adbshell.tap(point)
                print("微信添加")
                state = 3

        elif (state == 3):
            point = findpic.getLoc(src_img, find_src + r"\weixinsaoyisao.png")
            if point:
                adbshell.tap(point)
                print("微信扫一扫")
                state = 3
            pass

    pass
