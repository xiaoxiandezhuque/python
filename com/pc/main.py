import autopy
import win32api
import win32gui
import win32con
from PIL import Image

from com.pc import findpic
from com.pc import contrast_color
from com.pc.Bead import Bead

from com.pc import skill
from com.pc.bean import Point
from com.pc.bean import ReplacePoint
from com.pc import findbead
import autopy
from autopy.mouse import Button
import time
import random

from com.pc import pcclick


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


def sleepShort():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(6000, 8000) / 1000)


def quitThisGame(gameLoc):
    printPC("退出本次游戏")
    pcclick.downPoint((gameLoc[0] + random.randrange(768, 794), gameLoc[1] + random.randrange(44, 69)))
    sleepShort()
    pcclick.downPoint((gameLoc[0] + random.randrange(334, 486), gameLoc[1] + random.randrange(430, 479)))
    sleepShort()
    pcclick.downPoint((gameLoc[0] + random.randrange(444, 530), gameLoc[1] + random.randrange(381, 404)))
    pass


def printPC(str):
    print(str)


def distinguishBead(srcimg, beginX, beginY):
    otherBead = findpic.getAllLoc(srcimg, "./img/other.png")
    otherBead1 = findpic.getAllLoc(srcimg, "./img/other1.png")
    otherBead = otherBead | otherBead1
    redBead = findpic.getAllLoc(srcimg, "./img/red.png")
    buleBead = findpic.getAllLoc(srcimg, "./img/blue.png")
    grayBead = findpic.getAllLoc(srcimg, "./img/gray.png")
    greenBead = findpic.getAllLoc(srcimg, "./img/green.png")
    purpleBead = findpic.getAllLoc(srcimg, "./img/purple.png")
    beadList = [[0] * 8 for row in range(8)]
    for i in range(8):
        for j in range(8):
            xl = beginX + i * 59
            xr = beginX + (i + 1) * 59
            yt = beginY + j * 59
            yb = beginY + (j + 1) * 59
            for k in otherBead:
                if k[0] > xl and k[0] < xr and k[1] > yt and k[1] < yb:
                    beadList[i][j] = Bead.other
                    break
            if beadList[i][j]:
                continue
            for k in redBead:
                if k[0] > xl and k[0] < xr and k[1] > yt and k[1] < yb:
                    beadList[i][j] = Bead.red
                    break
            if beadList[i][j]:
                continue
            for k in buleBead:
                if k[0] > xl and k[0] < xr and k[1] > yt and k[1] < yb:
                    beadList[i][j] = Bead.blue
                    break
            if beadList[i][j]:
                continue
            for k in grayBead:
                if k[0] > xl and k[0] < xr and k[1] > yt and k[1] < yb:
                    beadList[i][j] = Bead.gray
                    break
            if beadList[i][j]:
                continue
            for k in greenBead:
                if k[0] > xl and k[0] < xr and k[1] > yt and k[1] < yb:
                    beadList[i][j] = Bead.green
                    break
            if beadList[i][j]:
                continue
            for k in purpleBead:
                if k[0] > xl and k[0] < xr and k[1] > yt and k[1] < yb:
                    beadList[i][j] = Bead.purple
                    break
            if beadList[i][j]:
                continue
            beadList[i][j] = Bead.yellow
    return beadList


replaceSet5 = set()
replaceSet4 = set()
replaceSet3 = set()
cPoint = (172 + 15, 103 + 15)

beginX, beginY = 0, 0
# 公主技能打的点
gongzhupoint1, gongzhupoint2 = False, False

count_no_bead = 0
count_games = 0

img_src = "./img/newpic.png"
movePointAgain = ReplacePoint(1, Point(1, 1), Point(1, 1))


def beginGame():
    global cPoint, replaceSet5, replaceSet4, replaceSet3, beginX, beginY, gongzhupoint1, gongzhupoint2
    global img_src
    global count_no_bead, count_games
    global movePointAgain
    while True:
        # try:
        #     Image.open(img_src).save("oldpic.png")
        # except FileNotFoundError as e:
        #     print("没有找到之前的图片")
        replaceSet5.clear()
        replaceSet4.clear()
        replaceSet3.clear()

        gameLoc = findWinLoc("gemsofwar")
        # print("游戏窗口的位置 ")
        # print(gameLoc)
        autopy.bitmap.capture_screen().save(img_src)

        #  这里有点小问题
        # if findpic.getLoc(img_src, "oldpic.png"):
        #     print("之前和现在的界面一样")
        # downPoint((gameLoc[0] + random.randrange(450, 600), gameLoc[1] + random.randrange(200, 500)))
        # continue

        # 需要刷的石头城市 点击
        btnNext = findpic.getLoc(img_src, "./img/needshitou.png")
        if btnNext:
            printPC("点击刷的城市")
            pcclick.downPoint(btnNext)
            sleepShort()
            pcclick.downPoint((gameLoc[0] + random.randrange(413, 657), gameLoc[1] + random.randrange(221, 345)))
            sleepShort()
            continue

        # 断线重连的  图标
        btnNext = findpic.getLoc(img_src, "./img/again.png")
        if btnNext:
            sleepLong()
            sleepLong()
        # 继续 按钮
        btnNext = findpic.getLoc(img_src, "./img/next0.png")
        if btnNext:
            printPC("点击继续")
            pcclick.downPoint(btnNext)
            sleepLong()
            continue
        # 提升等级  按钮
        btnNext = findpic.getLoc(img_src, "./img/next2.png")
        if btnNext:
            printPC("点击 提升等级")
            pcclick.downPoint(btnNext)
            sleepShort()
            # 点击出现的选择灵珠
            pcclick.downPoint((gameLoc[0] + random.randrange(450, 600), gameLoc[1] + random.randrange(200, 500)))
            sleepShort()
            continue
        # 准备战斗 按钮
        btnNext = findpic.getLoc(img_src, "./img/next3.png")
        if btnNext:
            printPC("点击 准备战斗")
            pcclick.downPoint(btnNext)
            gongzhupoint1 = False
            gongzhupoint2 = False
            count_games += 1
            print("游戏次数%s" % (count_games))
            sleepLong()
            continue
        # 重试  按钮
        btnNext = findpic.getLoc(img_src, "./img/next4.png")
        if btnNext:
            printPC("点击 重试")
            pcclick.downPoint(btnNext)
            sleepLong()
            sleepLong()
            continue
        # 在来一场  按钮
        btnNext = findpic.getLoc(img_src, "./img/next5.png")
        if btnNext:
            printPC("点击 在来一场")
            pcclick.downPoint(btnNext)
            sleepShort()
            continue

        # 看看图有没有进入消除界面
        if findpic.getLoc(img_src, "./img/other.png") or \
                findpic.getLoc(img_src, "./img/gray.png") or \
                findpic.getLoc(img_src, "./img/red.png"):
            count_no_bead = 0
            pass
        else:
            count_no_bead += 1
            print("画面中没有珠子")
            if count_no_bead >= 9:
                exit("连续没有珠子的次数太多，退出")
            pcclick.downPoint((gameLoc[0] + random.randrange(450, 600), gameLoc[1] + random.randrange(200, 500)))
            sleepLong()
            continue

        # 判断是否有技能
        # 龙魂的技能
        skillPointLonghun = findpic.getLoc(img_src, "./img/longhun.png")
        if skillPointLonghun:
            printPC("点击 龙魂技能")
            pcclick.downPoint(skillPointLonghun)
            sleepShort()
            autopy.bitmap.capture_screen().save(img_src)
            btnNext = findpic.getLoc(img_src, "./img/next1.png")
            if btnNext:
                sleepShort()
                pcclick.downPoint(btnNext)

            else:
                print("没有出现施法按钮")
            sleepLong()
            continue
        else:
            srcImage = Image.open(img_src)
            srcImage.crop((gameLoc[0], gameLoc[1], gameLoc[2] / 2, gameLoc[3])).save("./img/myplace.png")
            if not findpic.getLoc("./img/myplace.png", "./img/longhun_no.png") and \
                    findpic.getLoc("./img/myplace.png", "./img/card_die.png"):
                # 退出这一把,开始下一把
                quitThisGame(gameLoc)
                sleepShort()
                continue

        # 公主的技能
        skillPointGongzhu = findpic.getLoc(img_src, "./img/gongzhu.png")
        if skillPointGongzhu and (not gongzhupoint1 or not gongzhupoint2):
            printPC("点击 公主技能")
            pcclick.downPoint(skillPointGongzhu)
            sleepShort()
            autopy.bitmap.capture_screen().save(img_src)
            btnNext = findpic.getLoc(img_src, "./img/next1.png")
            if btnNext:
                sleepShort()
                pcclick.downPoint(btnNext)
                sleepShort()
                if not gongzhupoint2:
                    gongzhupoint2 = True
                    pcclick.downPoint((gameLoc[0] + random.randrange(60, 130), gameLoc[1] + random.randrange(480, 580)))
                else:
                    gongzhupoint1 = True
                    pcclick.downPoint((gameLoc[0] + random.randrange(60, 130), gameLoc[1] + random.randrange(350, 450)))
            else:
                print("没有出现施法按钮")
            sleepLong()
            continue

        # 原始点
        # baseBeadList = [[Bead.yellow, Bead.yellow, Bead.green, Bead.bule, Bead.purple, Bead.green, Bead.gray, Bead.red],
        #                 [Bead.other, Bead.green, Bead.gray, Bead.red, Bead.bule, Bead.other, Bead.gray, Bead.other],
        #                 [Bead.purple, Bead.yellow, Bead.bule, Bead.bule, Bead.red, Bead.gray, Bead.purple, Bead.purple],
        #                 [Bead.yellow, Bead.other, Bead.green, Bead.red, Bead.red, Bead.green, Bead.green, Bead.bule],
        #                 [Bead.yellow, Bead.red, Bead.gray, Bead.bule, Bead.other, Bead.yellow, Bead.gray, Bead.bule],
        #                 [Bead.red, Bead.purple, Bead.green, Bead.gray, Bead.gray, Bead.red, Bead.green, Bead.purple],
        #                 [Bead.gray, Bead.gray, Bead.bule, Bead.gray, Bead.bule, Bead.red, Bead.yellow, Bead.other],
        #                 [Bead.other, Bead.red, Bead.purple, Bead.other, Bead.green, Bead.gray, Bead.green, Bead.purple]]

        # pointColor = srcImage.getpixel((cPoint[0] + 59 * 0, cPoint[1] + 59 * 6))
        # print(pointColor)
        # color = contrast_color.get_color(pointColor)
        # print(color)
        # exit()
        beadList = [[0] * 8 for row in range(8)]
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
        replaceSet5, replaceSet4, replaceSet3 = findbead.find345(beadList)
        # 先消除4  5连击
        replacePoint5 = findbead.findColorsReplacePoint(replaceSet5, findcolors)
        if replacePoint5:
            printPC("消除5 连")
            if movePointAgain and myequest(movePointAgain, replacePoint5):
                replacePoint5 = findbead.findColorsReplacePoint(replaceSet5, findcolors)
                if replacePoint5:
                    movePointAgain = replacePoint5

                    pcclick.movePoint(replacePoint5, beginX, beginY)
                    sleepLong()
                    return
            else:
                movePointAgain = replacePoint5
                pcclick.movePoint(replacePoint5, beginX, beginY)
                sleepLong()
                continue
        replacePoint4 = findbead.findColorsReplacePoint(replaceSet4, findcolors)
        if replaceSet4:
            printPC("消除4 连")
            if movePointAgain and myequest(movePointAgain, replacePoint4):
                replacePoint4 = findbead.findColorsReplacePoint(replaceSet4, findcolors)
                if replacePoint4:
                    movePointAgain = replacePoint4
                    pcclick.movePoint(replacePoint4, beginX, beginY)
                    sleepLong()
                    continue
            else:
                movePointAgain = replacePoint4
                pcclick.movePoint(replacePoint4, beginX, beginY)
                sleepLong()
                continue

        # 卡组的技能
        # transitionList = skill.colorTransition(beadList, Bead.red, Bead.bule)

        replacePoint3 = findbead.findColorsReplacePoint(replaceSet3, findcolors)
        if replacePoint3:
            printPC("消除3 连")
            if movePointAgain and myequest(movePointAgain, replacePoint3):
                replacePoint3 = findbead.findColorsReplacePoint(replaceSet3, findcolors)
                if replacePoint3:
                    movePointAgain = replacePoint3
                    pcclick.movePoint(replacePoint3, beginX, beginY)
                    sleepLong()
                    continue
            else:
                movePointAgain = replacePoint3
                pcclick.movePoint(replacePoint3, beginX, beginY)
                sleepLong()
                continue


def myequest(a, o):
    if a.color != o.color:
        return False
    if a.fromPoint.x != o.fromPoint.x:
        return False
    if a.fromPoint.y != o.fromPoint.y:
        return False
    if a.toPoint.x != o.toPoint.x:
        return False
    if a.toPoint.y != o.toPoint.y:
        return False
    return True


def tesTFindBead():
    global cPoint
    bengintime = int(round(time.time() * 1000))
    # 原始点
    baseBeadList = [[Bead.yellow, Bead.other, Bead.gray, Bead.red, Bead.purple, Bead.purple, Bead.gray, Bead.other],
                    [Bead.gray, Bead.red, Bead.other, Bead.blue, Bead.yellow, Bead.blue, Bead.green, Bead.yellow],
                    [Bead.gray, Bead.green, Bead.red, Bead.yellow, Bead.gray, Bead.purple, Bead.blue, Bead.green],
                    [Bead.other, Bead.yellow, Bead.blue, Bead.blue, Bead.red, Bead.yellow, Bead.gray, Bead.purple],
                    [Bead.red, Bead.red, Bead.green, Bead.green, Bead.gray, Bead.green, Bead.other, Bead.gray],
                    [Bead.red, Bead.gray, Bead.other, Bead.red, Bead.other, Bead.blue, Bead.green, Bead.other],
                    [Bead.yellow, Bead.blue, Bead.gray, Bead.yellow, Bead.blue, Bead.red, Bead.yellow, Bead.green],
                    [Bead.red, Bead.red, Bead.green, Bead.other, Bead.purple, Bead.other, Bead.green, Bead.blue]]

    beadList = [[0] * 8 for row in range(8)]
    # pointColor = srcImage.getpixel((cPoint[0] + 59 * 0, cPoint[1] + 59 * 6))
    # print(pointColor)
    # color = contrast_color.get_color(pointColor)
    # print(color)
    # exit()
    srcImage = Image.open("./img/4.png")
    beginX = cPoint[0]
    beginY = cPoint[1]
    # beadList = distinguishBead("./img/4.png", beginX, beginY)

    # print(beadList)

    # 识别图片中的球
    for i in range(8):
        for j in range(8):
            # 找点的颜色  进行匹配，区分出是什么珠子
            pointColor = srcImage.getpixel((beginX + 59 * i, beginY + 59 * j))
            color = contrast_color.get_color(pointColor)
            # print(color)
            beadList[i][j] = color
            # color = beadList[i][j]
            if not baseBeadList[i][j] == color:
                print("在（%s,%s）点颜色不一样，识别的颜色是%s，本来的颜色是%s" % (i, j, color, baseBeadList[i][j]))
                # print(pointColor)

            # if i == 7 and j == 3:
            #     print((beginX + 59 * i, beginY + 59 * j))
            #     print(pointColor)
            # if i == 7 and j == 5:
            #     print((beginX + 59 * i, beginY + 59 * j))
            #     print(pointColor)

        # print("位置是%s,%s，点颜色%s,识别出来的颜色%s,应该是的颜色%s" % (i, j, pointColor, color, baseBeadList[i][j]))

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

    overtime = int(round(time.time() * 1000))
    print("识别需要的时间%s" % (overtime - bengintime))
    return baseBeadList


if __name__ == "__main__":
    # beginGame()
    tesTFindBead()
    # beadList = tesTFindBead()
    # replaceSet5, replaceSet4, replaceSet3 = findbead.find345(beadList)
    # for beadPoint in replaceSet5:
    #     print(beadPoint)
    #
    # print("----------------------")
    # for beadPoint in replaceSet4:
    #     print(beadPoint)

    # print(replaceSet5)
    # print(replaceSet4)
    # print(replaceSet3)
    # beginGame()
    #     autopy.bitmap.capture_screen().save(r"./img/111111.png")
    #     img = Image.open(r"./img/111111.png")
    #     img.crop((0,0,1000,1200)).save(r"./img/2222.png")

    pass
