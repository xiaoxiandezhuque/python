from com.pc.bean import Point
from com.pc.bean import ReplacePoint
import random


# 找 34连   返回一个集合
def find345(beadList):
    replaceSet5, replaceSet4, replaceSet3 = set(), set(), set()
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
    find5(beadList, replaceSet4, replaceSet5)

    return (replaceSet5, replaceSet4, replaceSet3)


# 根据4连找5连
def find5(beadList, replaceSet4, replaceSet5):
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
                if color == lColor and x - 2 >= 0 and beadList[x - 2][y] == color:
                    if color == tColor and y - 2 >= 0 and beadList[x][y - 2] == color:
                        if color == rColor == bColor:
                            if random.randrange(2) == 0:
                                replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x + 1, y)))
                            else:
                                replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y + 1)))
                        if color == rColor:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x + 1, y)))
                        elif color == bColor:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y + 1)))
                    elif color == bColor and y + 2 <= 7 and beadList[x][y + 2] == color:
                        if color == rColor == tColor:
                            if random.randrange(2) == 0:
                                replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x + 1, y)))
                            else:
                                replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y - 1)))
                        if color == rColor:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x + 1, y)))
                        elif color == tColor:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y - 1)))
                    elif color == rColor and x + 2 <= 7 and beadList[x + 2][y] == color:
                        if color == tColor == bColor:
                            if random.randrange(2) == 0:
                                replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y + 1)))
                            else:
                                replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y - 1)))
                        if color == tColor:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y - 1)))
                        elif color == bColor:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y + 1)))
                elif color == tColor and y - 2 >= 0 and beadList[x][y - 2] == color:
                    if color == bColor and y + 2 <= 7 and beadList[x][y + 2] == color:
                        if color == rColor == lColor:
                            if random.randrange(2) == 0:
                                replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x + 1, y)))
                            else:
                                replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x - 1, y)))
                        if color == rColor:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x + 1, y)))
                        elif color == lColor:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x - 1, y)))
                    elif color == rColor and x + 2 <= 7 and beadList[x + 2][y] == color:
                        if color == lColor == bColor:
                            if random.randrange(2) == 0:
                                replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x - 1, y)))
                            else:
                                replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y + 1)))
                        if color == lColor:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x - 1, y)))
                        elif color == bColor:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y + 1)))
                elif (color == rColor and x + 2 <= 7 and beadList[x + 2][y] == color) and \
                        (color == bColor and y + 2 <= 7 and beadList[x][y + 2] == color):
                    if color == lColor == tColor:
                        if random.randrange(2) == 0:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x - 1, y)))
                        else:
                            replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y - 1)))
                    if color == lColor:
                        replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x - 1, y)))
                    elif color == tColor:
                        replaceSet5.add(ReplacePoint(color, Point(x, y), Point(x, y - 1)))


def print4(i, j, locstr):
    # print("位置(%s,%s)有4连以上（包括4）,这个点换%s面的点" % (i, j, locstr))
    pass


def print3(i, j, locstr):
    # print("位置(%s,%s)有3连,这个点换%s面的点" % (i, j, locstr))
    pass


def findColorsReplacePoint(replaceSet, colors):
    if replaceSet:
        for color in colors:
            for replacePoint in replaceSet:
                if color == replacePoint.color:
                    replaceSet.remove(replacePoint)
                    return replacePoint
        return replaceSet.pop()
