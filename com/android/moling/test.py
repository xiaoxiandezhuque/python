import os
import threading
import time
from com.android import findpic


def saveScreenshot(name):
    os.system("adb -s 127.0.0.1:62001 shell screencap -p /sdcard/%s" % name)  # 截屏
    # os.system(r"adb pull /sdcard/%s C:\work\python\com\android\moling\img" % name)  # 导出图片
    os.system(r"adb -s 127.0.0.1:62001 pull /sdcard/%s %s\img" % (name, os.getcwd()))  # 导出图片



if __name__ == "__main__":
    #  kill    force-stop
    #  先返回home  在 kill
    # os.system("adb -s 127.0.0.1:62025  shell am kill com.netease.my")


    # saveScreenshot("13.png")
    src_img = "./img/12.png"
    playPoint = findpic.getLoc(src_img, "./dengji25.png")
    if playPoint:
        print("x=" + str(playPoint[0]) + "    y=" + str(playPoint[1]))
