import os
import random


def tap(pointX, pointY):
    # os.system("adb shell input tap %s %s" % (pointX, pointY))
    os.system("adb -s 127.0.0.1:62001  shell input swipe %s %s %s %s  %s" % (
        pointX, pointY, pointX, pointY, random.randrange(80, 200)))


def input(str):
    os.system("adb -s 127.0.0.1:62001  shell input text %s" % (str))


#  3  home   4 back
def tapKey(keyevent):
    os.system("adb -s 127.0.0.1:62001  shell input keyevent  %s" % (keyevent))


def swipe(fromX, fromY, toX, toY):
    a = fromY - fromX
    os.system("adb -s 127.0.0.1:62001  shell input swipe %s %s %s %s  %s" % (
        fromX, fromY, toX, toY, random.randrange(a if a > 80 else 80, 1000)))


if __name__ == "__main__":
    tap(100, 200)
    swipe(100, 300, 100, 300)
