import os
import random
import time
from builtins import print

from com.android import findpic
from com.android import adbshell


def saveScreenshot(name):
    os.system("adb shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb pull /sdcard/%s C:\work\python\com\android\yinyangshi\img" % name)  # 导出图片


def sleepLittle():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 10000) / 1000)


def sleepGameTime():
    time.sleep(random.randrange(90000, 180000) / 1000)


def getRandomNumber(fromNum, toNum):
    return round(random.uniform(fromNum, toNum), 5)


def printThis(str):
    print(str)


src_img = "./img/1.png"

if __name__ == "__main__":
    # print("111")
    # 判断链接设备

    machine = os.popen("adb devices")
    machineStr = machine.read()
    print(machineStr)
    if ("device" not in machineStr):
        exit("还没连接到设备")
    # 获取当前的屏幕截图
    while True:

        saveScreenshot("1.png")
        # 精英怪
        playPoint = findpic.getLoc(src_img, "./img/bossplay.png")
        if playPoint:
            printThis("精英怪")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLong()
            continue

        # 小怪
        playPoint = findpic.getCenterLoc(src_img, "./img/play.png")
        if playPoint:
            printThis("小怪")
            print(playPoint)
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLong()
            continue
        # 找对话窗口  缩小
        playPoint = findpic.getCenterLoc(src_img, "./img/suoxiao.png")
        if playPoint:
            printThis("找对话窗口  缩小")
            print(playPoint)
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue
        #  点击探索按钮
        playPoint = findpic.getLoc(src_img, "./img/begin.png")
        if playPoint:
            printThis("点击探索按钮")
            printThis(playPoint)
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue

        #  找盒子
        playPoint = findpic.getLoc(src_img, "./img/hezi.png")
        if playPoint:
            printThis("找盒子")
            printThis(playPoint)
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLong()
            adbshell.tap(getRandomNumber(200, 1000), getRandomNumber(500, 600))
            sleepLong()
            continue
        # 游戏结束的画面
        playPoint = findpic.getLoc(src_img, "./img/over.png")
        if playPoint:
            printThis("游戏结束的画面")
            adbshell.tap(getRandomNumber(200, 1000), getRandomNumber(300, 600))
            sleepLittle()
            continue


        # 找体力图标
        playPoint = findpic.getLoc(src_img, "./img/huadong.png")
        if playPoint:
            printThis("找体力图标")

            adbshell.tap(getRandomNumber(200, 1200), getRandomNumber(300, 530))
            # adbshell.swipe(getRandomNumber(700, 1200), getRandomNumber(100, 650)
            #                , getRandomNumber(100, 550), getRandomNumber(100, 650))
            sleepLong()
            continue
        playPoint = findpic.getLoc(src_img, "./img/16.png")
        if playPoint:
            printThis("找16章")

            adbshell.tap(playPoint[0], playPoint[1])
            # adbshell.swipe(getRandomNumber(700, 1200), getRandomNumber(100, 650)
            #                , getRandomNumber(100, 550), getRandomNumber(100, 650))
            sleepLittle()
            continue
        sleepLong()
    # adbshell.tap("30.6061","460.6061")
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
