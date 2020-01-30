from tkinter import *
import threading
import os
import random
import time

from com.android import findpic
from com.android import adbshell
from com.android.moling import myUtils
from com.android.moling.PlayGouLiang import PlayGouLiang
from com.android.moling.PlayLong import PlayLong

isGet = True


<<<<<<< HEAD
def saveScreenshot(name):
    os.system("adb  shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb  pull /sdcard/%s %s/img" % (name, os.getcwd()))  # 导出图片


def sleepLittle():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 10000) / 1000)


def getRandomNumber(fromNum, toNum):
    return round(random.uniform(fromNum, toNum), 5)


=======
>>>>>>> 97e3d1653566fe09268b3070c0ad57991c6a43a4
def printThis(str):
    lb.insert(END, str)
    print(str)


# 4星  76次
# 困难2552经验一次 大概33次   33*4=132体力  84216经验 3星
# 2星怪  15次1
# 3900经验 地狱  2星 10次    3星 22次   4星50次   6
count = 0
all = 331  # 55
countMoney = 0
allMoney = 0  # 控制买几管体力`

countFail = 0  # 失败次数

out_time = 900
game_begin_agein = 0
src_img = r"C:\Users\Administrator\Nox_share\Image\1.png"

gameState = 0
playWay = PlayLong(src_img)

# 0 从礼物想获取  1 从商店购买
getTili = 0

isOpenGame = False


def countGame():
    global count, all, game_begin_agein, sleepTime
    game_begin_agein = time.time()
    count += 1
    setLabelText(count, countFail, countMoney, "还没退出")
    if count >= all:
        exitPrint("游戏的次数已到上限")
    time.sleep(random.randrange(sleepTime * 1000, (sleepTime + 10) * 1000) / 1000)


def exitPrint(content):
    setLabelText(count, countFail, countMoney, content)
<<<<<<< HEAD
    btn_begin['bg'] = "#ffffff"
    btn_end['bg'] = "#ff0000"
    global isBengin
=======
    btn_begin['bg'] = "white"
    btn_end['bg'] = "red"
    global isBengin, isOpenGame
    # isOpenGame = False
>>>>>>> 97e3d1653566fe09268b3070c0ad57991c6a43a4
    isBengin = False
    # musicPlay.play()


def beginGame():
    global count, all, countMoney, allMoney, countFail, out_time, game_begin_agein, isBengin, playWay, src_img \
        , getTili, isOpenGame
    # 判断链接设备

    machine = os.popen("adb devices")
    machineStr = machine.read()
    setLabelText(count, countFail, countMoney, machineStr)
    count = 0
    countFail = 0
    if ("device" not in machineStr):
        exitPrint("还没连接到设备")
    # 获取当前的屏幕截图
    game_begin_agein = time.time()

    while True:
        if (not isBengin):
            return
        myUtils.saveScreenshot("1.png")

        playPoint = findpic.getLoc(src_img, "./img/dakaishangdian.png")
        if playPoint:
            printThis("打开商店   购买体力")
            count -= 1
            if countMoney > allMoney:
                exitPrint("不能再买体力了 兄弟")
                return
            if getTili == 0:
                adbshell.tap(myUtils.getRandomNumber(670, 849), myUtils.getRandomNumber(416, 474))
                myUtils.sleepLittle()
                myUtils.saveScreenshot("1.png")
                playPointChild = findpic.getLoc(src_img, "./img/shouqu.png")
                if playPointChild:
                    adbshell.tap(playPointChild[0], playPointChild[1])
                    myUtils.sleepLittle()
                    adbshell.tap(playPointChild[0], playPointChild[1])
                    myUtils.sleepLittle()
                    # 关闭保管箱
                    adbshell.tap(myUtils.getRandomNumber(903, 939), myUtils.getRandomNumber(121, 152))
                    myUtils.sleepLittle()
                    continue
                else:
                    adbshell.tap(myUtils.getRandomNumber(903, 939), myUtils.getRandomNumber(121, 152))
                    getTili = 1
                    myUtils.sleepLittle()
                    continue
            else:
                countMoney += 1
                adbshell.tap(playPoint[0], playPoint[1])
                myUtils.sleepLittle()
                adbshell.tap(myUtils.getRandomNumber(444, 616), myUtils.getRandomNumber(266, 460))
                myUtils.sleepLittle()
                adbshell.tap(myUtils.getRandomNumber(455, 600), myUtils.getRandomNumber(416, 458))
                myUtils.sleepLittle()
                adbshell.tap(myUtils.getRandomNumber(578, 707), myUtils.getRandomNumber(410, 460))
                myUtils.sleepLittle()
                adbshell.tap(myUtils.getRandomNumber(477, 701), myUtils.getRandomNumber(600, 641))
                myUtils.sleepLittle()
                adbshell.tap(myUtils.getRandomNumber(581, 701), myUtils.getRandomNumber(640, 641))
                myUtils.sleepLittle()
                continue

        if not isOpenGame:
            playPoint = findpic.getLoc(src_img, "./img/begin.png")
            if playPoint:
                isOpenGame = True
                continue

            playPoint = findpic.getLoc(src_img, "./img/moling.png")
            if playPoint:
                printThis("打开魔灵召唤")
                adbshell.tap(playPoint[0], playPoint[1])
                time.sleep(60)
                continue
            playPoint = findpic.getLoc(src_img, "./img/buzaitishi.png")
            if playPoint:
                printThis("关闭不再提示")
                adbshell.tap(playPoint[0], playPoint[1])
                myUtils.sleepLittle()
                continue

            playPoint = findpic.getLoc(src_img, "./img/molingzhaohuan.png")
            if playPoint:
                printThis("找到进入游戏的页面")
                adbshell.tap(myUtils.getRandomNumber(300, 800), myUtils.getRandomNumber(600, 700))
                myUtils.sleepLittle()
                adbshell.tapKey(4)
                myUtils.sleepLittle()
                adbshell.tapKey(4)
                myUtils.sleepLittle()
                adbshell.tapKey(4)
                myUtils.sleepLittle()
                continue
            playPoint = findpic.getLoc(src_img, "./img/fou.png")
            if playPoint:
                printThis("点击是否退出 的 否")
                adbshell.tap(playPoint[0], playPoint[1])
                myUtils.sleepLittle()
                continue

            playPoint = findpic.getLoc(src_img, "./img/play.png")
            if playPoint:
                printThis("去刷龙10")
                adbshell.tap(myUtils.getRandomNumber(692, 746), myUtils.getRandomNumber(630, 683))
                myUtils.sleepLittle()
                adbshell.tap(myUtils.getRandomNumber(635, 765), myUtils.getRandomNumber(570, 640))
                myUtils.sleepLittle()
                continue

            playPoint = findpic.getLoc(src_img, "./img/long10.png")
            if playPoint:
                printThis("找战斗按钮")
                adbshell.tap(myUtils.getRandomNumber(1027, 1100), playPoint[1])
                myUtils.sleepLittle()
                continue

            playPoint = findpic.getLoc(src_img, "./img/long.png")
            if playPoint:
                printThis("龙 地下城")
                adbshell.tap(playPoint[0], playPoint[1])
                myUtils.sleepLong()
                continue
            pass

        if playWay.begin():
            continue
        playPoint = findpic.getLoc(src_img, "./img/begin.png")
        if playPoint:
            printThis("开始战斗")
            adbshell.tap(playPoint[0], playPoint[1])
            countGame()
            continue
            #  再来一次
        playPoint = findpic.getLoc(src_img, "./img/xiayiceng.png")
        if playPoint:
            printThis("下一层")
            adbshell.tap(playPoint[0], playPoint[1])
            myUtils.sleepLittle()
            continue
        playPoint = findpic.getLoc(src_img, "./img/again.png")
        if playPoint:
            printThis("再来一次")
            adbshell.tap(playPoint[0], playPoint[1])
            countGame()
            continue

        playPoint = findpic.getLoc(src_img, "./img/jixuzhandou.png")
        if playPoint:
            printThis("继续战斗")
            adbshell.tap(playPoint[0], playPoint[1])
            myUtils.sleepLong()
            continue

        playPoint = findpic.getLoc(src_img, "./img/zhandouzhunb.png")
        if playPoint:
            printThis("战斗失败之后的战斗准备")
            countFail += 1
            adbshell.tap(playPoint[0], playPoint[1])
            myUtils.sleepLong()
            continue

        playPoint = findpic.getLoc(src_img, "./img/shi.png")
        if playPoint:
            printThis("确定出售的  是 按钮")
            adbshell.tap(playPoint[0], playPoint[1])
            myUtils.sleepLittle()
            continue
        if playWay.isGetGoods():
            continue
        # if (isGet):
        #     playPoint = findpic.getLoc(src_img, "./img/get.png")
        #     if playPoint:
        #         printThis("获得道具")
        #         adbshell.tap(playPoint[0], playPoint[1])
        #         myUtils.sleepLittle()
        #         continue
        # else:
        #     playPoint = findpic.getLoc(src_img, "./img/chushou1.png")
        #     if playPoint:
        #         printThis("出售")
        #         adbshell.tap(playPoint[0], playPoint[1])
        #         myUtils.sleepLittle()
        #         continue

        playPoint = findpic.getLoc(src_img, "./img/sure.png")
        if playPoint:
            printThis("确认")
            adbshell.tap(playPoint[0], playPoint[1])
            myUtils.sleepLittle()
            continue

        playPoint = findpic.getLoc(src_img, "./img/sure1.png")
        if playPoint:
            printThis("确认1")
            adbshell.tap(playPoint[0], playPoint[1])
            myUtils.sleepLittle()
            continue

        playPoint = findpic.getLoc(src_img, "./img/shengli.png")
        if playPoint:
            printThis("胜利")
            adbshell.tap(myUtils.getRandomNumber(500, 600), myUtils.getRandomNumber(60, 500))
            myUtils.sleepLittle()
            adbshell.tap(myUtils.getRandomNumber(500, 600), myUtils.getRandomNumber(60, 500))
            myUtils.sleepLittle()
            continue

        playPoint = findpic.getLoc(src_img, "./img/shibai.png")
        if playPoint:
            printThis("游戏失败 重开")
            adbshell.tap(myUtils.getRandomNumber(700, 930), myUtils.getRandomNumber(430, 500))
            myUtils.sleepLittle()
            continue

        playPoint = findpic.getLoc(src_img, "./img/huidatohome.png")
        if playPoint:
            printThis("回答问题，去桌面关闭，重开")
            adbshell.tapKey(3)
            os.system(
                "adb -s 127.0.0.1:62001  shell am force-stop com.com2us.smon.normal.freefull.google.kr.android.common")
            isOpenGame = False
            myUtils.sleepLittle()
            continue
        playPoint = findpic.getLoc(src_img, "./img/banbengengxing.png")
        if playPoint:
            printThis("版本更新的确定")
            adbshell.tap(playPoint[0], playPoint[1])
            time.sleep(60)
            isOpenGame = False
            continue

        if (time.time() - game_begin_agein > out_time):
            exitPrint("游戏超时")



        print("随便点击一下")
        adbshell.tap(myUtils.getRandomNumber(300, 800), myUtils.getRandomNumber(600, 700))
        myUtils.sleepLong()
        pass


tk = Tk()
tk.title("魔灵")
isBengin = False


def createLabelAndEntry(labelText):
    fm = Frame(tk, bg="white", padx=15, pady=8)
    Label(fm, text=labelText, bg="white", width=20).pack(side=LEFT)
    e = StringVar()
    Entry(fm, textvariable=e, width=20).pack(side=LEFT, fill=X, expand=YES)
    fm.pack(side=TOP, fill=X)
    return e


def createLabel(fm):
    label = Label(fm, text="", bg="white", width=30, height=10, justify=LEFT)
    label.pack(side=LEFT, expand=NO)
    return label


def setLabelText(allCount, failCount, bugCount, exitReason):
    label['text'] = "总次数:　　　　%s\n" \
                    "失败次数:　　　%s\n" \
                    "购买体力次数:　%s\n" \
                    "上次记录时间:　%s\n" \
                    "退出原因:　　　%s\n" \
                    % (allCount, failCount, bugCount, time.strftime("%H:%M:%S"), exitReason)


def createList(fm):
    lb = Listbox(fm, width=20, height=10)
    lb.pack(side=LEFT)
    sl = Scrollbar(fm)
    sl.pack(side=LEFT, fill=Y)
    sl['command'] = lb.yview
    lb['yscrollcommand'] = sl.set
    return lb


def crtateBtn():
    global btn_begin, btn_end
    fm = Frame(tk, bg="white")
    Button(fm, text="地狱2x", command=clickHuoshan2).pack(side=LEFT, fill=X, expand=NO)
    Button(fm, text="地狱3x", command=clickHuoshan3).pack(side=LEFT, fill=X, expand=NO)
    Button(fm, text="地狱4x", command=clickHuoshan4).pack(side=LEFT, fill=X, expand=NO)
    Button(fm, text="巨10", command=clickJuren).pack(side=LEFT, fill=X, expand=NO)
    Button(fm, text="龙10", command=clickLong).pack(side=LEFT, fill=X, expand=NO)
    Button(fm, text="保存设置", command=clickSave).pack(side=LEFT, fill=X, expand=NO, padx=20)
    fm.pack(side=TOP, fill=X, ipady=20, ipadx=20)

    btn_begin = Button(tk, text="开始", command=clickBegin, height=2)
    btn_begin.pack(side=TOP, fill=X, pady=8)
    btn_end = Button(tk, text="结束", command=clickEnd, height=2)
    btn_end.pack(side=TOP, fill=X)


def clickHuoshan2():
    global playWay
    eSV1.set("45")
    eSV3.set("10")
    playWay = PlayGouLiang(src_img)


def clickHuoshan3():
    global playWay
    eSV1.set("45")
    eSV3.set("22")
    playWay = PlayGouLiang(src_img)


def clickHuoshan4():
    global playWay
    eSV1.set("45")
    eSV3.set("50")
    playWay = PlayGouLiang(src_img)


def clickJuren():
    global playWay
    playWay = PlayLong(src_img)
    eSV1.set("180")


def clickLong():
    global playWay
    playWay = PlayLong(src_img)
    eSV1.set("80")


def clickSave():
    global sleepTime, all, allMoney, out_time
    sleepTime = int(eSV1.get())
    # sleepTime = 10
    allMoney = int(eSV2.get())
    all = int(eSV3.get())
    out_time = int(eSV4.get())


def clickBegin():
    global isBengin, playWay, src_img
    if (eSV1.get() and eSV2.get() and eSV3.get() and eSV4.get()):
        lb.delete(0, END)  # 清空列表
        setLabelText(0, 0, 0, "开始了")
        btn_begin['bg'] = "red"
        btn_end['bg'] = "white"
        clickSave()

        isBengin = True
        tThread = threading.Thread(target=beginGame)
        tThread.setDaemon(True)
        tThread.start()


def clickEnd():
    exitPrint("手动结束")


def setDefult():
    eSV1.set("80")
    eSV2.set("10")
    eSV3.set("220")
    eSV4.set("900")
    setLabelText(0, 0, 0, "还没有开始")


eSV1 = createLabelAndEntry("沉睡时间")
eSV2 = createLabelAndEntry("购买体力次数")
eSV3 = createLabelAndEntry("重复的最大次数")
eSV4 = createLabelAndEntry("超时时间")

fmLabel = Frame(tk, bg="white", padx=15, pady=8)
label = createLabel(fmLabel)
lb = createList(fmLabel)
fmLabel.pack(side=TOP, fill=X)

crtateBtn()

setDefult()

# Label(app, text=e.get(), bg="white").pack(side=LEFT)
# canvas = Canvas(tk, width=400, height=400, bg='white')
# canvas.pack()
# crtateBtn(tk)

# b = Button(tk,Text ="ok",COMMAND=callback())
# btn_juren = Button(tk, text="巨人10", command=callback).pack(side=TOP, anchor=W, fill=X, expand=NO)
# # btn_huoshan = Button(tk, text="火山地狱", command=callback).pack()

# t = threading.Thread(target=close)
# t.start()
tk.mainloop()
