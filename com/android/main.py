import os
import time

from com.android import findpic
from com.android import adbshell


def saveScreenshot(name):
    os.system("adb shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb pull /sdcard/%s C:\work\python\com\android" % name)  # 导出图片


if __name__ == "__main__":
    # 判断链接设备
    machine = os.popen("adb devices")
    machineStr = machine.read()
    if ("device" not in machineStr):
        exit("还没连接到设备")
    # 获取当前的屏幕截图
    saveScreenshot("1.png")

    playPoint = findpic.getLoc("1.png", "./moling/img/ok.png")
    if playPoint:
        print(playPoint)
        # adbshell.tap(playPoint[0], playPoint[1])

    # 匹配截图和目标图片
    # loc = findpic.getLoc("1.png", "wx.png")
    # if loc:
    #     adbshell.tap(loc[0], loc[1])
    # else:
    #     print('没有找到匹配的图片')
    #
    # # adbshell.tap(257, 421)
    # # adbshell.input("1111")
    # time.sleep(2)
    # print("完成")
