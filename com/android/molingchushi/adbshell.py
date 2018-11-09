import os
import random


def tap(port, pointX, pointY):
    # os.system("adb shell input tap %s %s" % (pointX, pointY))
    os.system("adb -s 127.0.0.1:%s  shell input swipe %s %s %s %s  %s" % (
        port, pointX, pointY, pointX, pointY, random.randrange(80, 200)))


def input(port, str):
    os.system("adb -s 127.0.0.1:%s  shell input text %s" % (port, str))


#  3  home   4 back
def tapKey(port, keyevent):
    os.system("adb -s 127.0.0.1:%s  shell input keyevent  %s" % (port, keyevent))


def swipe(port, fromX, fromY, toX, toY):
    a = fromY - fromX
    os.system("adb -s 127.0.0.1:%s  shell input swipe %s %s %s %s  %s" % (
        port, fromX, fromY, toX, toY, random.randrange(a if a > 80 else 80, 1000)))


if __name__ == "__main__":
    tap(100, 200)
    swipe(100, 300, 100, 300)
