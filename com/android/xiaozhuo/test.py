import os
import threading
import time
from com.android import findpic
from com.android import adbshell


def saveScreenshot(name):
    os.system("adb  shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb pull /sdcard/%s E:\work\python\com\android\xiaozhuo\img" % name)  # 导出图片
    # os.system(r"adb -s 127.0.0.1:62001 pull /sdcard/%s %s\img" % (name, os.getcwd()))  # 导出图片


def takeSecond(elem):
    return elem[0]

src_img = r"E:\work\python\com\android\xiaozhuo\img\11.png"
find_src = r"E:\work\python\com\android\xiaozhuo\img"

if __name__ == "__main__":
    # saveScreenshot("24.png")
    a = findpic.getAllLoc(src_img,find_src+r"\5tie2.png")
    print(a)
    pass
