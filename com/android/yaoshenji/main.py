import os
import random
import time

from com.android import findpic
from com.android import adbshell


def saveScreenshot(name):
    os.system("adb shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb pull /sdcard/%s C:\work\python\com\android\yaoshenji\img" % name)  # 导出图片


def sleepLittle():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 10000) / 1000)


def sleepGameTime():
    time.sleep(random.randrange(90000, 180000) / 1000)

def sleepLittle():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 10000) / 1000)


def sleepGameTime():
    time.sleep(random.randrange(27000, 30000) / 1000)


def getRandomNumber(fromNum, toNum):
    return round(random.uniform(fromNum, toNum), 5)


def printThis(str):
    print(str)


# 982,588    1070，650
src_img = "./img/1.png"

if __name__ == "__main__":

    # 判断链接设备
    machine = os.popen("adb devices")
    machineStr = machine.read()
    print(machineStr)
    if ("device" not in machineStr):
        exit("还没连接到设备")
    # 获取当前的屏幕截图

    while True:
        saveScreenshot("1.png")

        playPoint = findpic.getLoc(src_img, "./img/kaizhan.png")
        if playPoint:
            printThis("点击  开战 按钮")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepGameTime()
            continue

        playPoint = findpic.getLoc(src_img, "./img/tiaozhan.png")
        if playPoint:
            printThis("点击  挑战  按钮")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLong()
            continue
        playPoint = findpic.getLoc(src_img, "./img/100baozi.png")
        if playPoint:
            #这图只能找到30包子   通过+y坐标来点击100包子
            printThis("点击  点击100包子补充体力 按钮")
            adbshell.tap(playPoint[0], playPoint[1])#+113
            sleepLong()
            continue

        playPoint = findpic.getLoc(src_img, "./img/zailaiyici.png")
        if playPoint:
            printThis("点击  再来一次  按钮")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLong()
            continue

        printThis("游戏成功")
        adbshell.tap(getRandomNumber(600,1000),getRandomNumber(600,700))
        sleepLittle()
        printThis("随便点击一下")
        adbshell.tap(getRandomNumber(600,1000),getRandomNumber(600,700))
        sleepLong()
        printThis("进入")
        adbshell.tap(getRandomNumber(754,1000),getRandomNumber(544,644))
        sleepLong()
        printThis("进入")
        adbshell.tap(getRandomNumber(754,1000),getRandomNumber(544,644))
        sleepLong()

