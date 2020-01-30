from tkinter import *
from tkinter import ttk
import threading
import os
import random
import time

from com.android import findpic
from com.android.menghuanxiyou import adbshell

srcImg = "%s/img/mh.png" % os.getcwd()


def saveScreenshot(name):
    os.system("adb -s 127.0.0.1:62025 shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb -s 127.0.0.1:62025 pull /sdcard/%s %s\img" % (name, os.getcwd()))  # 导出图片


def sleepLittle():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 10000) / 1000)


def getRandomNumber(fromNum, toNum):
    return round(random.uniform(fromNum, toNum), 5)


def exitPrint(content):
    printThis(content)


def printThis(str):
    print(str)


def sanjieqiyuan():
    global srcImg
    while (True):

        playPoint = findpic.getLoc(srcImg, "./img/sanjieqiyuanwancheng.png")
        if (playPoint):
            printThis("三界奇缘完成")
            adbshell.tap(getRandomNumber(1124, 1159), getRandomNumber(33, 62))
            sleepLittle()
            return
        playPoint = findpic.getLoc(srcImg, "./img/sanjieqiyuan.png")
        if (playPoint):
            printThis("三界奇缘")
            adbshell.tap(getRandomNumber(959, 1080), getRandomNumber(206, 332))
            sleepLittle()
            continue
        return


def beginGame():
    global srcImg

    while (True):
        saveScreenshot("mh.png")

        playPoint = findpic.getLoc(srcImg, "./img/zhengzaizhandouzhong.png")
        if (playPoint):
            printThis("正在战斗中")
            sleepLong()
            continue
        playPoint = findpic.getLoc(srcImg, "./img/duihuakuang.png")
        if (playPoint):
            printThis("对话框")
            adbshell.tap(getRandomNumber(1052, 1186), getRandomNumber(58, 70))
            sleepLittle()
            continue
        playPoint = findpic.getLoc(srcImg, "./img/queding.png")
        if (playPoint):
            printThis("确定")
            adbshell.tap(playPoint[0], playPoint[1])
            # 确定 有可能是点击了 三界奇缘
            sanjieqiyuan()
            sleepLong()
            continue

        playPoint = findpic.getLoc(srcImg, "./img/shiyong.png")
        if (playPoint):
            printThis("使用")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLong()
            continue

        playPoint = findpic.getLoc(srcImg, "./img/xuanzheyaozuodeshi.png")
        if (playPoint):
            printThis("选择要做的事")
            adbshell.tap(playPoint[0] + 50, playPoint[1] + 75)
            sleepLong()
            continue

        playPoint = findpic.getLoc(srcImg, "./img/goumai.png")
        if (playPoint):
            printThis("购买")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue
        playPoint = findpic.getLoc(srcImg, "./img/shangjiao.png")
        if (playPoint):
            printThis("上交")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue

        # playPoint = findpic.getLoc(srcImg, "./img/sanjieqiyuan.png")
        # if (playPoint):
        #     printThis("三界奇缘")
        #     adbshell.tap(getRandomNumber(959, 1080), getRandomNumber(206, 332))
        #     sleepLittle()
        #     continue

        playPoint = findpic.getLoc(srcImg, "./img/guanbi.png")
        if (playPoint):
            printThis("关闭")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue
        playPoint = findpic.getLoc(srcImg, "./img/zidong.png")
        if (playPoint):
            printThis("自动战斗")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLong()
            continue

        # adbshell.tap(getRandomNumber(1063, 1200), getRandomNumber(200, 240))
        adbshell.tap(getRandomNumber(1063, 1200), getRandomNumber(290, 330))
        sleepLittle()


pass

if __name__ == "__main__":
    # saveScreenshot("12.png")
    beginGame()
