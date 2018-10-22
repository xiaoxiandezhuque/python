import os
import threading
import time


def saveScreenshot(name):
    os.system("adb -s 127.0.0.1:62001 shell screencap -p /sdcard/%s" % name)  # 截屏
    # os.system(r"adb pull /sdcard/%s C:\work\python\com\android\moling\img" % name)  # 导出图片
    os.system(r"adb -s 127.0.0.1:62001 pull /sdcard/%s %s\img" % (name, os.getcwd()))  # 导出图片

if __name__=="__main__":
    saveScreenshot("11.png")
