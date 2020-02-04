import os
import random


def tap(point):
    # os.system("adb shell input tap %s %s" % (pointX, pointY))
    os.system("adb   shell input swipe %s %s %s %s  %s" % (
        point[0], point[1], point[0], point[1], random.randrange(80, 200)))


def tap(pointX, pointY):
    # os.system("adb shell input tap %s %s" % (pointX, pointY))
    os.system("adb   shell input swipe %s %s %s %s  %s" % (
        pointX, pointY, pointX, pointY, random.randrange(80, 200)))


def input(str):
    os.system("adb   shell input text %s" % (str))


#  3  home   4 back
def tapKey(keyevent):
    os.system("adb   shell input keyevent  %s" % (keyevent))


def swipe(fromX, fromY, toX, toY):
    a = fromY - fromX
    os.system("adb   shell input swipe %s %s %s %s  %s" % (
        fromX, fromY, toX, toY, random.randrange(a if a > 80 else 80, 1000)))


if __name__ == "__main__":
    tap(100, 200)
    swipe(100, 300, 100, 300)
