import os
import threading
import time
from com.android import findpic
from com.android import adbshell


def saveScreenshot(name):
    os.system("adb -s 127.0.0.1:62001 shell screencap -p /mnt/shared/Image/%s" % name)  # 截屏
    # os.system(r"adb pull /sdcard/%s C:\work\python\com\android\moling\img" % name)  # 导出图片
    # os.system(r"adb -s 127.0.0.1:62001 pull /sdcard/%s %s\img" % (name, os.getcwd()))  # 导出图片


def takeSecond(elem):
    return elem[0]


if __name__ == "__main__":
    # saveScreenshot("15.png")
    os.system("adb -s 127.0.0.1:62025  shell input keyevent  3" )
    os.system("adb -s 127.0.0.1:62025  shell am force-stop com.sjyt.oilmanager")
    # os.system(r"adb -s 127.0.0.1:62025 pull /sdcard/%s %s\img" % ("123321.png", os.getcwd()))  # 导出图片

    #  kill    force-stop
    #  先返回home  在 kill
    # os.system("adb -s 127.0.0.1:62025  shell am kill com.netease.my")
    # t1= time.time()
    # os.system("adb -s 127.0.0.1:62025 shell screencap -p /mnt/shared/Image/%s" % "1111.png")
    # saveScreenshot("1111.png")
    # t2 = time.time()
    # print(int(round(t2 * 1000))-int(round(t1 * 1000)))
    # src_img = "./img/12.png"
    # playPoint = findpic.getLoc(src_img, "./dengji25.png")
    # if playPoint:
    #     print("x=" + str(playPoint[0]) + "    y=" + str(playPoint[1]))
    # a = set({(3, 3), (2, 2)})
    # b = list(a)
    # b.sort(key=takeSecond)
    # print(b)
    pass
