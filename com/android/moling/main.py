import os
import random
import time

from com.android import findpic
from com.android import adbshell
from com.music import main as musicPlay


def saveScreenshot(name):
    os.system("adb -s 127.0.0.1:62001 shell screencap -p /sdcard/%s" % name)  # 截屏
    # os.system(r"adb pull /sdcard/%s C:\work\python\com\android\moling\img" % name)  # 导出图片
    os.system(r"adb -s 127.0.0.1:62001 pull /sdcard/%s %s\img" % (name, os.getcwd()))  # 导出图片


def sleepLittle():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 10000) / 1000)


def getRandomNumber(fromNum, toNum):
    return round(random.uniform(fromNum, toNum), 5)


def printThis(str):
    print(str)


# 982,588    1070，650
src_img = "./img/1.png"

# 4星  76次
# 困难2552经验一次 大概33次   33*4=132体力  84216经验 3星
# 2星怪  15次1
# 3900经验 地狱  2星 10次    3星 22次   4星50次   6
count = 0
all = 331  # 55
countMoney = 0
allMoney = 0  # 控制买几管体力`

countFail = 0  # 失败次数

out_time = 900
game_begin_agein = 0


def countGame():
    global count, all, game_begin_agein

    game_begin_agein = time.time()
    count += 1
    print("游戏次数   " + str(count))
    print("游戏失败次数   " + str(countFail))
    print("购买体力次数" + str(countMoney))
    if count >= all:
        exitPrint("游戏的次数已到上限")
    # time.sleep(random.randrange(35000, 40000) / 1000)  # 2星
    # time.sleep(random.randrange(45000, 50000) / 1000)  # 3星
    # time.sleep(random.randrange(110000, 130000) / 1000)  # 魔力
    # time.sleep(random.randrange(180000, 200000) / 1000)  # 巨人7层
    time.sleep(random.randrange(220000, 240000) / 1000)  # 巨人10层


def exitPrint(content):
    print("---------------------------------------")
    print("当前游戏次数" + str(count))
    print("游戏失败次数" + str(countFail))
    print("购买体力次数" + str(countMoney))
    print("游戏结束时间" + time.strftime("%H:%M:%S"))
    print(content)
    # musicPlay.play()
    exit(content)


def beginGame():
    global src_img, count, all, countMoney, allMoney, countFail, out_time, game_begin_agein
    # 判断链接设备
    machine = os.popen("adb devices")
    machineStr = machine.read()
    print(machineStr)
    if ("device" not in machineStr):
        exit("还没连接到设备")
    # 获取当前的屏幕截图
    game_begin_agein = time.time()
    while True:
        saveScreenshot("1.png")
        return
        #  战斗
        # playPoint = findpic.getLoc(src_img, "./img/play.png")
        # if playPoint:
        #     printThis("点击  战斗 按钮")
        #     adbshell.tap(playPoint[0], playPoint[1])
        #     sleepLittle()
        #     adbshell.swipe(getRandomNumber(1000, 1100), getRandomNumber(500, 600), getRandomNumber(500, 550),
        #                    getRandomNumber(500, 600))
        #     sleepLittle()
        #     adbshell.swipe(getRandomNumber(1000, 1100), getRandomNumber(500, 600), getRandomNumber(500, 550),
        #                    getRandomNumber(500, 600))
        #     sleepLittle()
        #     continue
        #
        # playPoint = findpic.getLoc(src_img, "./img/huoshan.png")
        # if playPoint:
        #     printThis("点击  火山 按钮")
        #     adbshell.tap(playPoint[0], playPoint[1])
        #     sleepLittle()
        #     adbshell.tap(getRandomNumber(1143, 1208), getRandomNumber(228, 286))
        #     sleepLittle()
        #     continue

        playPoint = findpic.getLoc(src_img, "./img/dakaishangdian.png")
        if playPoint:
            printThis("打开商店   购买体力")
            count -= 1
            countMoney += 1
            if countMoney > allMoney:
                exitPrint("不能再买体力了 兄弟")

            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            adbshell.tap(getRandomNumber(444, 616), getRandomNumber(266, 460))
            sleepLittle()
            adbshell.tap(getRandomNumber(455, 600), getRandomNumber(416, 458))
            sleepLittle()
            adbshell.tap(getRandomNumber(578, 707), getRandomNumber(410, 460))
            sleepLittle()
            adbshell.tap(getRandomNumber(477, 701), getRandomNumber(600, 641))
            sleepLittle()
            adbshell.tap(getRandomNumber(581, 701), getRandomNumber(640, 641))
            sleepLittle()
            continue

        playPoint = findpic.getLoc(src_img, "./img/begin.png")
        if playPoint:
            printThis("开始战斗")
            adbshell.tap(playPoint[0], playPoint[1])
            countGame()
            continue
            #  再来一次
        playPoint = findpic.getLoc(src_img, "./img/again.png")
        if playPoint:
            printThis("再来一次")
            adbshell.tap(playPoint[0], playPoint[1])
            countGame()
            continue

        playPoint = findpic.getLoc(src_img, "./img/jixuzhandou.png")
        if playPoint:
            printThis("继续战斗")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLong()
            continue
        playPoint = findpic.getLoc(src_img, "./img/zhandouzhunb.png")
        if playPoint:
            printThis("战斗失败之后的战斗准备")
            countFail += 1
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLong()
            continue

        # playPoint = findpic.getLoc(src_img, "./img/shi.png")
        # if playPoint:
        #     printThis("确定出售的  是 按钮")
        #     adbshell.tap(playPoint[0], playPoint[1])
        #     sleepLittle()
        #     continue
        playPoint = findpic.getLoc(src_img, "./img/get.png")
        if playPoint:
            printThis("获得道具")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue
        # playPoint = findpic.getLoc(src_img, "./img/chushou1.png")
        # if playPoint:
        #     printThis("出售")
        #     adbshell.tap(playPoint[0], playPoint[1])
        #     sleepLittle()
        #     continue
        playPoint = findpic.getLoc(src_img, "./img/sure.png")
        if playPoint:
            printThis("确认")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue

        playPoint = findpic.getLoc(src_img, "./img/shengli.png")
        if playPoint:
            printThis("胜利")
            adbshell.tap(getRandomNumber(500, 600), getRandomNumber(60, 500))
            sleepLittle()
            adbshell.tap(getRandomNumber(500, 600), getRandomNumber(60, 500))
            sleepLittle()
            continue

        playPoint = findpic.getLoc(src_img, "./img/shibai.png")
        if playPoint:
            printThis("游戏失败 重开")
            adbshell.tap(getRandomNumber(700, 930), getRandomNumber(430, 500))
            sleepLittle()
            continue

        if (time.time() - game_begin_agein > out_time):
            exitPrint("游戏超时")

        printThis("随便点击一下")
        adbshell.tap(getRandomNumber(500, 600), getRandomNumber(60, 500))
        sleepLong()

        pass

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

