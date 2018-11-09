import os
import random
import time


def saveScreenshot(port, name):
    os.system("adb -s 127.0.0.1:%s shell screencap -p /mnt/shared/Image/%s" % (port, name))  # 截屏


def sleepLittle():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 10000) / 1000)


def getRandomNumber(fromNum, toNum):
    return round(random.uniform(fromNum, toNum), 5)
