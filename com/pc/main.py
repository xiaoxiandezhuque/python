from builtins import print

import autopy
import win32api
import win32gui
import win32con
from PIL import Image

from com.pc import findpic
import contrast_color
from Bead import Bead

from com.pc import skill
from com.pc.bean import Point
from com.pc.bean import ReplacePoint
import autopy
from autopy.mouse import Button
import time
import random


def findWinLoc(name):
    window_title = name
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    hwnd = win32gui.FindWindow(win32con.NULL, window_title)
    if hwnd == 0:
        exit("没有找到这个窗口")
    window_left, window_top, window_right, window_bottom = win32gui.GetWindowRect(hwnd)
    if min(window_left, window_top) < 0 \
            or window_right > screen_width \
            or window_bottom > screen_height:
        exit("窗口最小化或者超出当前屏幕，请重新调整窗口的位子")
    loc = (window_left, window_top, window_right, window_bottom)

    return loc


def print4(i, j, locstr):
    # print("位置(%s,%s)有4连以上（包括4）,这个点换%s面的点" % (i, j, locstr))
    pass


def print3(i, j, locstr):
    # print("位置(%s,%s)有3连,这个点换%s面的点" % (i, j, locstr))
    pass


# 找 34连   返回一个集合
def find345(beadList):
    global replaceSet4, replaceSet3
    for i in range(8):
        for j in range(8):
            lColor, rColor, tColor, bColor = False, False, False, False

            if (i - 1 >= 0):
                lColor = beadList[i - 1][j]
            if (i + 1 <= 7):
                rColor = beadList[i + 1][j]
            if (j - 1 >= 0):
                tColor = beadList[i][j - 1]
            if (j + 1 <= 7):
                bColor = beadList[i][j + 1]

            if lColor and lColor == rColor:
                if lColor == bColor:
                    if (i - 2 >= 0 and beadList[i - 2][j] == lColor) or (i + 2 <= 7 and beadList[i + 2][j] == lColor):
                        print4(i, j, "下")
                        replaceSet4.add(ReplacePoint(bColor, Point(i, j), Point(i, j + 1)))
                    else:
                        print3(i, j, "下")
                        replaceSet3.add(ReplacePoint(bColor, Point(i, j), Point(i, j + 1)))
                if lColor == tColor:
                    if (i - 2 >= 0 and beadList[i - 2][j] == lColor) or (i + 2 <= 7 and beadList[i + 2][j] == lColor):
                        print4(i, j, "上")
                        replaceSet4.add(ReplacePoint(tColor, Point(i, j), Point(i, j - 1)))
                    else:
                        print3(i, j, "上")
                        replaceSet3.add(ReplacePoint(tColor, Point(i, j), Point(i, j - 1)))
            if tColor and tColor == bColor:
                if tColor == lColor:
                    if (j - 2 >= 0 and beadList[i][j - 2] == tColor) or (j + 2 <= 7 and beadList[i][j + 2] == tColor):
                        print4(i, j, "左")
                        replaceSet4.add(ReplacePoint(lColor, Point(i, j), Point(i - 1, j)))
                    else:
                        print3(i, j, "左")
                        replaceSet3.add(ReplacePoint(lColor, Point(i, j), Point(i - 1, j)))
                if tColor == rColor:
                    if (j - 2 >= 0 and beadList[i][j - 2] == tColor) or (j + 2 <= 7 and beadList[i][j + 2] == tColor):
                        print4(i, j, "右")
                        replaceSet4.add(ReplacePoint(rColor, Point(i, j), Point(i + 1, j)))
                    else:
                        print3(i, j, "右")
                        replaceSet3.add(ReplacePoint(rColor, Point(i, j), Point(i + 1, j)))

            if i - 2 >= 0:
                llColor = beadList[i - 2][j]
                if llColor == lColor:
                    if lColor == rColor:
                        print3(i, j, "右")
                        replaceSet3.add(ReplacePoint(rColor, Point(i, j), Point(i + 1, j)))
                    elif lColor == tColor:
                        print3(i, j, "上")
                        replaceSet3.add(ReplacePoint(tColor, Point(i, j), Point(i, j - 1)))
                    elif lColor == bColor:
                        print3(i, j, "下")
                        replaceSet3.add(ReplacePoint(bColor, Point(i, j), Point(i, j + 1)))
            if i + 2 <= 7:
                rrColor = beadList[i + 2][j]
                if rrColor == rColor:
                    if rColor == lColor:
                        print3(i, j, "左")
                        replaceSet3.add(ReplacePoint(lColor, Point(i, j), Point(i - 1, j)))
                    elif rColor == tColor:
                        print3(i, j, "上")
                        replaceSet3.add(ReplacePoint(tColor, Point(i, j), Point(i, j - 1)))
                    elif rColor == bColor:
                        print3(i, j, "下")
                        replaceSet3.add(ReplacePoint(bColor, Point(i, j), Point(i, j + 1)))
            if j - 2 >= 0:
                ttColor = beadList[i][j - 2]
                if ttColor == tColor:
                    if tColor == lColor:
                        print3(i, j, "左")
                        replaceSet3.add(ReplacePoint(lColor, Point(i, j), Point(i - 1, j)))
                    elif tColor == rColor:
                        print3(i, j, "右")
                        replaceSet3.add(ReplacePoint(rColor, Point(i, j), Point(i + 1, j)))
                    elif tColor == bColor:
                        print3(i, j, "下")
                        replaceSet3.add(ReplacePoint(bColor, Point(i, j), Point(i, j + 1)))

            if j + 2 <= 7:
                bbColor = beadList[i][j + 2]
                if bbColor == bColor:
                    if bColor == lColor:
                        print3(i, j, "左")
                        replaceSet3.add(ReplacePoint(lColor, Point(i, j), Point(i - 1, j)))
                    elif bColor == rColor:
                        print3(i, j, "右")
                        replaceSet3.add(ReplacePoint(rColor, Point(i, j), Point(i + 1, j)))
                    elif bColor == tColor:
                        print3(i, j, "上")
                        replaceSet3.add(ReplacePoint(tColor, Point(i, j), Point(i, j - 1)))
    find5(beadList)


# 根据4连找5连
def find5(beadList):
    global replaceSet5, replaceSet4
    if replaceSet4:
        for c in replaceSet4:
            color, x, y = c.color, c.fromPoint.x, c.fromPoint.y
            lColor, rColor, tColor, bColor = False, False, False, False
            if x - 1 >= 0:
                lColor = beadList[x - 1][y]
            if x + 1 <= 7:
                rColor = beadList[x + 1][y]
            if y - 1 >= 0:
                tColor = beadList[x][y - 1]
            if y + 1 <= 7:
                bColor = beadList[x][y + 1]
            if lColor == rColor == tColor == bColor:
                if x - 2 >= 0 and beadList[x - 2][y] == color:
                    replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x + 1, y)))
                if x + 2 <= 7 and beadList[x + 2][y] == color:
                    replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x - 1, y)))
                if y - 2 >= 0 and beadList[x][y - 2] == color:
                    replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y + 1)))
                if y + 2 <= 7 and beadList[x][y + 2] == color:
                    replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y - 1)))
            else:
                if (color == lColor and x - 2 >= 0 and beadList[x - 2][y] == color) or \
                        (color == rColor and x + 2 <= 7 and beadList[x + 2][y] == color):
                    if bColor == color:
                        replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y + 1)))
                    elif tColor == color:
                        replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y - 1)))
                if (color == tColor and y - 2 >= 0 and beadList[x][y - 2] == color) or \
                        (color == bColor and y + 2 <= 7 and beadList[x][y + 2] == color):
                    if lColor == color:
                        replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x - 1, y)))
                    elif rColor == color:
                        replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x + 1, y)))


def findColorsReplacePoint(replaceSet, colors):
    if replaceSet:
        for color in colors:
            for replacePoint in replaceSet:
                if color == replacePoint.color:
                    return replacePoint
        return replaceSet.pop()


def movePoint(replacePoint):
    # print("移动点（%s，%s）到（%s，%s），颜色是%s"
    #       % (replacePoint.fromPoint.x, replacePoint.fromPoint.y, replacePoint.toPoint.x, replacePoint.toPoint.y,
    #          replacePoint.color))
    global beginX, beginY

    autopy.mouse.smooth_move(beginX + replacePoint.fromPoint.x * 59 + random.randrange(10, 40),
                             beginY + replacePoint.fromPoint.y * 59 + random.randrange(10, 40))
    autopy.mouse.toggle(Button.LEFT, True)
    time.sleep(random.randrange(300, 1000) / 1000)
    autopy.mouse.smooth_move(beginX + replacePoint.toPoint.x * 59 + random.randrange(10, 40),
                             beginY + replacePoint.toPoint.y * 59 + random.randrange(10, 40))
    time.sleep(random.randrange(100, 300) / 1000)
    autopy.mouse.toggle(Button.LEFT, False)
    pass


def downPoint(point):
    autopy.mouse.smooth_move(point[0], point[1])
    autopy.mouse.toggle(Button.LEFT, True)
    time.sleep(random.randrange(100, 300) / 1000)
    autopy.mouse.toggle(Button.LEFT, False)


def sleepShort():
    time.sleep(random.randrange(1000, 2000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 8000) / 1000)


replaceSet5 = set()
replaceSet4 = set()
replaceSet3 = set()
cPoint = (172 + 15, 103 + 15)

beginX, beginY = 0, 0
# 公主技能打的点
gongzhupoint1, gongzhupoint2 = False, False


def beginGame():
    global cPoint, replaceSet5, replaceSet4, replaceSet3, beginX, beginY, gongzhupoint1, gongzhupoint2
    while True:
        try:
            Image.open("newpic.png").save("oldpic.png")
        except FileNotFoundError as e:
            print("没有找到之前的图片")
        replaceSet5.clear()
        replaceSet4.clear()
        replaceSet3.clear()
        sleepLong()
        gameLoc = findWinLoc("gemsofwar")
        # print("游戏窗口的位置 ")
        # print(gameLoc)
        autopy.bitmap.capture_screen().save("newpic.png")

        #  这里有点小问题
        # if findpic.getLoc("newpic.png", "oldpic.png"):
        #     print("之前和现在的界面一样")
        # downPoint((gameLoc[0] + random.randrange(450, 600), gameLoc[1] + random.randrange(200, 500)))
        # continue

        btnNext = findpic.getLoc("newpic.png", "again.png")
        if btnNext:
            sleepLong()
            sleepLong()

        btnNext = findpic.getLoc("newpic.png", "next0.png")
        if btnNext:
            downPoint(btnNext)
            continue
        btnNext = findpic.getLoc("newpic.png", "next2.png")
        if btnNext:
            downPoint(btnNext)
            continue
        btnNext = findpic.getLoc("newpic.png", "next3.png")
        if btnNext:
            downPoint(btnNext)
            gongzhupoint1 = False
            gongzhupoint2 = False
            continue
        btnNext = findpic.getLoc("newpic.png", "next4.png")
        if btnNext:
            downPoint(btnNext)
            sleepLong()
            continue
        btnNext = findpic.getLoc("newpic.png", "next5.png")
        if btnNext:
            downPoint(btnNext)
            sleepLong()
            continue

        # 看看图有没有进入消除界面
        if findpic.getLoc("newpic.png", "other.png"):
            pass
        else:
            print("画面中没有珠子")
            downPoint((gameLoc[0] + random.randrange(450, 600), gameLoc[1] + random.randrange(200, 500)))
            continue

        # 判断是否有技能
        # 龙魂的技能
        skillPointLonghun = findpic.getLoc("newpic.png", "longhun.png")
        if skillPointLonghun:
            downPoint(skillPointLonghun)
            sleepShort()
            autopy.bitmap.capture_screen().save("newpic.png")
            btnNext = findpic.getLoc("newpic.png", "next1.png")
            if btnNext:
                sleepShort()
                downPoint(btnNext)

            else:
                print("没有出现施法按钮")
            continue
        # 公主的技能
        skillPointGongzhu = findpic.getLoc("newpic.png", "gongzhu.png")
        if skillPointGongzhu and (not gongzhupoint1 or not gongzhupoint2):
            downPoint(skillPointGongzhu)
            sleepShort()
            autopy.bitmap.capture_screen().save("newpic.png")
            btnNext = findpic.getLoc("newpic.png", "next1.png")
            if btnNext:
                sleepShort()
                downPoint(btnNext)
                sleepShort()
                if not gongzhupoint2:
                    gongzhupoint2 = True
                    downPoint((gameLoc[0] + random.randrange(60, 130), gameLoc[1] + random.randrange(480, 580)))
                else:
                    gongzhupoint1 = True
                    downPoint((gameLoc[0] + random.randrange(60, 130), gameLoc[1] + random.randrange(350, 450)))
            else:
                print("没有出现施法按钮")
            continue

        srcImage = Image.open("newpic.png")

        # 原始点
        # baseBeadList = [[Bead.yellow, Bead.yellow, Bead.green, Bead.bule, Bead.purple, Bead.green, Bead.gray, Bead.red],
        #                 [Bead.other, Bead.green, Bead.gray, Bead.red, Bead.bule, Bead.other, Bead.gray, Bead.other],
        #                 [Bead.purple, Bead.yellow, Bead.bule, Bead.bule, Bead.red, Bead.gray, Bead.purple, Bead.purple],
        #                 [Bead.yellow, Bead.other, Bead.green, Bead.red, Bead.red, Bead.green, Bead.green, Bead.bule],
        #                 [Bead.yellow, Bead.red, Bead.gray, Bead.bule, Bead.other, Bead.yellow, Bead.gray, Bead.bule],
        #                 [Bead.red, Bead.purple, Bead.green, Bead.gray, Bead.gray, Bead.red, Bead.green, Bead.purple],
        #                 [Bead.gray, Bead.gray, Bead.bule, Bead.gray, Bead.bule, Bead.red, Bead.yellow, Bead.other],
        #                 [Bead.other, Bead.red, Bead.purple, Bead.other, Bead.green, Bead.gray, Bead.green, Bead.purple]]
        beadList = [[0] * 8 for row in range(8)]
        # pointColor = srcImage.getpixel((cPoint[0] + 59 * 0, cPoint[1] + 59 * 6))
        # print(pointColor)
        # color = contrast_color.get_color(pointColor)
        # print(color)
        # exit()

        beginX = gameLoc[0] + cPoint[0]
        beginY = gameLoc[1] + cPoint[1]
        # 识别图片中的球
        for i in range(8):
            for j in range(8):
                # 找点的颜色  进行匹配，区分出是什么珠子
                pointColor = srcImage.getpixel((beginX + 59 * i, beginY + 59 * j))
                color = contrast_color.get_color(pointColor)
                # print(color)
                # if baseBeadList[i][j] == color:
                beadList[i][j] = color

                # if i==2 and j==5:
                #     print((beginX + 59 * i, beginY + 59 * j))
                #     print(pointColor)
                # if i==3 and j==7:
                #     print((beginX + 59 * i, beginY + 59 * j))
                #     print(pointColor)
                # else:
                #     print("位置是%s,%s，点颜色%s,识别出来的颜色%s,应该是的颜色%s" % (i, j, pointColor, color, baseBeadList[i][j]))

                # if color == "RED":
                #     beads[i][j] = Bead.red
        # print(contrast_color.get_color(c))
        # print(beadList[0])
        # print(beadList[1])
        # print(beadList[2])
        # print(beadList[3])
        # print(beadList[4])
        # print(beadList[5])
        # print(beadList[6])
        # print(beadList[7])
        # exit()

        # 卡组消除的颜色顺序
        findcolors = [Bead.other, Bead.purple, Bead.red]
        find345(beadList)
        # 先消除4  5连击
        replacePoint5 = findColorsReplacePoint(replaceSet5, findcolors)
        if replacePoint5:
            movePoint(replacePoint5)
            continue
        replacePoint4 = findColorsReplacePoint(replaceSet4, findcolors)
        if replaceSet4:
            movePoint(replacePoint4)
            continue

        # 卡组的技能
        # transitionList = skill.colorTransition(beadList, Bead.red, Bead.bule)

        replacePoint3 = findColorsReplacePoint(replaceSet3, findcolors)
        if replacePoint3:
            movePoint(replacePoint3)
            continue


if __name__ == "__main__":
    beginGame()
