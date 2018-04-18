import os


def tap(pointX, pointY):
    os.system("adb shell input tap %s %s" % (pointX, pointY))


def input(str):
    os.system("adb shell input text %s" % (str))

#  3  home   4 back
def tapKey(keyevent):
    os.system("adb shell input keyevent  %s" % (keyevent))


def swipe(fromX, fromY, toX, toY):
    os.system("adb shell input swipe %s %s %s %s" % (fromX, fromY, toX, toY))


if __name__ == "__main__":
   tapKey(5)