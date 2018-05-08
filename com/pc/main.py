import autopy
import win32api
import win32gui
import win32con
from PIL import Image

import findpic
import contrast_color
from Bead import Bead

from com.pc.bean import Point
from com.pc.bean import ReplacePoint


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
    print(loc)
    return loc


def print4(i, j, locstr):
    print("位置(%s,%s)有4连以上（包括4）,这个点换%s面的点" % (i, j, locstr))


def print3(i, j, locstr):
    print("位置(%s,%s)有3连,这个点换%s面的点" % (i, j, locstr))


# 找 34连   返回一个集合
def find345(beadList):
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
    print("移动点（%s，%s）到（%s，%s），颜色是%s"
          % (replacePoint.fromPoint.x, replacePoint.fromPoint.y, replacePoint.toPoint.x, replacePoint.toPoint.y,
             replacePoint.color))
    pass


replaceSet5 = set()
replaceSet4 = set()
replaceSet3 = set()

if __name__ == "__main__":
    # autopy.mouse.smooth_move(1, 1)
    # findWinLoc("GemsofWar")
    # print(Be)
    # loc = findpic.getLoc("yuantu.png", 'red.png')
    # print(loc)

    srcImage = Image.open("yuantu.png")
    # findpic.getLoc("yuantu.png","bule.png")
    # 原始点
    cPoint = (172 + 15, 103 + 15)
    baseBeadList = [[Bead.yellow, Bead.yellow, Bead.green, Bead.bule, Bead.purple, Bead.green, Bead.gray, Bead.red],
                    [Bead.other, Bead.green, Bead.gray, Bead.red, Bead.bule, Bead.other, Bead.gray, Bead.other],
                    [Bead.purple, Bead.yellow, Bead.bule, Bead.bule, Bead.red, Bead.gray, Bead.purple, Bead.purple],
                    [Bead.yellow, Bead.other, Bead.green, Bead.red, Bead.red, Bead.green, Bead.green, Bead.bule],
                    [Bead.yellow, Bead.red, Bead.gray, Bead.bule, Bead.other, Bead.yellow, Bead.gray, Bead.bule],
                    [Bead.red, Bead.purple, Bead.green, Bead.gray, Bead.gray, Bead.red, Bead.green, Bead.purple],
                    [Bead.gray, Bead.gray, Bead.bule, Bead.gray, Bead.bule, Bead.red, Bead.yellow, Bead.other],
                    [Bead.other, Bead.red, Bead.purple, Bead.other, Bead.green, Bead.gray, Bead.green, Bead.purple]]
    beadList = [[0] * 8 for row in range(8)]
    # pointColor = srcImage.getpixel((cPoint[0] + 59 * 0, cPoint[1] + 59 * 6))
    # print(pointColor)
    # color = contrast_color.get_color(pointColor)
    # print(color)
    # exit()
    # 识别图片中的球
    for i in range(8):
        for j in range(8):
            # 找点的颜色  进行匹配，区分出是什么珠子
            pointColor = srcImage.getpixel((cPoint[0] + 59 * i, cPoint[1] + 59 * j))
            color = contrast_color.get_color(pointColor)
            # print(color)
            if baseBeadList[i][j] == color:
                beadList[i][j] = color
            else:
                print("位置是%s,%s，点颜色%s,识别出来的颜色%s,应该是的颜色%s" % (i, j, pointColor, color, baseBeadList[i][j]))

            # if color == "RED":
            #     beads[i][j] = Bead.red
    # print(contrast_color.get_color(c))

    # 卡组消除的颜色顺序
    findcolors = [Bead.gray]
    #卡组的技能



    find345(beadList)

    replacePoint5 = findColorsReplacePoint(replaceSet5, findcolors)
    if replacePoint5:
        movePoint(replacePoint5)
    replacePoint4 = findColorsReplacePoint(replaceSet4, findcolors)
    if replaceSet4:
        movePoint(replacePoint4)
    replacePoint3 = findColorsReplacePoint(replaceSet3, findcolors)
    if replacePoint3:
        movePoint(replacePoint3)
