import os
import random
import time

from com.android import findpic
from com.android import adbshell


def saveScreenshot(name):
    os.system("adb shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb pull /sdcard/%s C:\work\python\com\android\moling\img" % name)  # 导出图片


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
    time.sleep(random.randrange(90000, 180000) / 1000)


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
        #  点击探索按钮
        playPoint = findpic.getLoc(src_img, "./img/play.png")
        if playPoint:
            printThis("点击  战斗 按钮")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue
        #  地下城
        playPoint = findpic.getLoc(src_img, "./img/fuben.png")
        if playPoint:
            printThis("点击  地下城 按钮")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue
        #  点击 龙  的界面
        playPoint = findpic.getLoc(src_img, "./img/long.png")
        if playPoint:
            printThis("点击  龙  按钮")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            adbshell.tap(getRandomNumber(982,1070),getRandomNumber(588,650))
            sleepLittle()
            continue

        #  获取道具
        playPoint = findpic.getLoc(src_img, "./img/get.png")
        if playPoint:
            printThis("获取道具")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue
        #  获取材料
        playPoint = findpic.getLoc(src_img, "./img/cailiao.png")
        if playPoint:
            printThis("获取材料")
            adbshell.tap(getRandomNumber(568,706), getRandomNumber(569,627))
            sleepLittle()
            continue

        #  再来一次
        playPoint = findpic.getLoc(src_img, "./img/again.png")
        if playPoint:
            printThis("再来一次")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue
        #  没体力了  点击充值
        playPoint = findpic.getLoc(src_img, "./img/meitili.png")
        if playPoint:
            printThis("没体力了  点击充值")
            
            adbshell.tap(getRandomNumber(452,600), getRandomNumber(407,463))
            sleepLittle()
            adbshell.tap(getRandomNumber(256,462), getRandomNumber(267,489))
            sleepLittle()
            adbshell.tap(getRandomNumber(445,601), getRandomNumber(417,457))
            sleepLittle()
            continue
        #  购买完毕
        playPoint = findpic.getLoc(src_img, "./img/goumai.png")
        if playPoint:
            printThis("购买完毕")
            adbshell.tap(getRandomNumber(469,709), getRandomNumber(407,463))
            sleepLittle()
            adbshell.tap(getRandomNumber(1048,1084), getRandomNumber(78,118))
            sleepLittle()
            continue
        #  彩虹怪
        playPoint = findpic.getLoc(src_img, "./img/caihongguai.png")
        if playPoint:
            printThis("彩虹怪")
            adbshell.tap(getRandomNumber(565,714), getRandomNumber(562,627))
            sleepLittle()
            continue

        #  开始战斗
        playPoint = findpic.getLoc(src_img, "./img/begin.png")
        if playPoint:
            printThis("开始战斗")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepGameTime()
            continue

        #  游戏胜利 结束
        playPoint = findpic.getLoc(src_img, "./img/ok.png")
        if playPoint:
            printThis("游戏胜利 结束")
            adbshell.tap(getRandomNumber(426,1111), getRandomNumber(328,620))
            sleepLittle()
            adbshell.tap(getRandomNumber(426,1111),getRandomNumber(328,620))
            sleepLittle()
            continue
        #  游戏胜利 结束
        playPoint = findpic.getLoc(src_img, "./img/shibai.png")
        if playPoint:
            printThis("游戏失败 重开")
            adbshell.tap(getRandomNumber(700,930),getRandomNumber(430,500))
            sleepLittle()
            continue
        printThis("随便点击一下")
        adbshell.tap(getRandomNumber(500,600),getRandomNumber(60,500))
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
