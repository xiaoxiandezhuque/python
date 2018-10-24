import os
import random
import time




def saveScreenshot(name):
    os.system("adb -s 127.0.0.1:62001 shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb -s 127.0.0.1:62001 pull /sdcard/%s %s\img" % (name, os.getcwd()))  # 导出图片


def sleepLittle():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 10000) / 1000)


def getRandomNumber(fromNum, toNum):
    return round(random.uniform(fromNum, toNum), 5)

