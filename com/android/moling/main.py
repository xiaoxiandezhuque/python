import os
import random
import time

from com.android import findpic
from com.android import adbshell


def saveScreenshot(name):
    os.system("adb shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb pull /sdcard/%s E:\work\python\main\android\moling\img" % name)  # 导出图片


def sleepLittle():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 10000) / 1000)


def sleepGameTime():
    time.sleep(random.randrange(90000, 180000) / 1000)


if __name__ == "__main__":
    # 判断链接设备
    machine = os.popen("adb devices")
    machineStr = machine.read()
    if ("device" not in machineStr):
        exit("还没连接到设备")
    # 获取当前的屏幕截图
    saveScreenshot("1.png")

    adbshell.tap("30.6061","460.6061")
    # 匹配截图和目标图片
    # loc = findpic.getLoc("./img/1.png", "wx.png")
    # if loc:
    #     adbshell.tap(loc[0], loc[1])
    # else:
    #     print('没有找到匹配的图片')
    #
    # adbshell.tap(257, 421)
    # adbshell.input("1111")
    # time.sleep(2)
    # print("完成")
