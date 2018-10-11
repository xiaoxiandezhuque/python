from tkinter import *
from tkinter import ttk
import threading
import os
import random
import time

from com.android import findpic
from com.android import adbshell
from com.music import main as musicPlay

isGet = True


def saveScreenshot(name):
    os.system("adb -s 127.0.0.1:62001 shell screencap -p /sdcard/%s" % name)  # 截屏
    os.system(r"adb -s 127.0.0.1:62001 pull /sdcard/%s %s\img" % (name, os.getcwd()))  # 导出图片


def sleepLittle():
    time.sleep(random.randrange(2000, 3000) / 1000)


def sleepLong():
    time.sleep(random.randrange(5000, 10000) / 1000)


def getRandomNumber(fromNum, toNum):
    return round(random.uniform(fromNum, toNum), 5)


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
    btn_begin['bg'] = "white"
    btn_end['bg'] = "red"
    global isBengin
    isBengin = False
    musicPlay.play()


def beginGame():
    global count, all, countMoney, allMoney, countFail, out_time, game_begin_agein, isBengin, isGet
    # 判断链接设备
    src_img = "%s/img/1.png" % os.getcwd()
    machine = os.popen("adb devices")
    machineStr = machine.read()
    setLabelText(count, countFail, countMoney, machineStr)
    if ("device" not in machineStr):
        exitPrint("还没连接到设备")
    # 获取当前的屏幕截图
    game_begin_agein = time.time()
    while True:
        if (not isBengin):
            return
        saveScreenshot("1.png")
        playPoint = findpic.getLoc(src_img, "./img/dakaishangdian.png")
        if playPoint:
            printThis("打开商店   购买体力")
            count -= 1
            countMoney += 1
            if countMoney > allMoney:
                exitPrint("不能再买体力了 兄弟")
                return

            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            adbshell.tap(getRandomNumber(444, 616), getRandomNumber(266, 460))
            sleepLittle()
            adbshell.tap(getRandomNumber(455, 600), getRandomNumber(416, 458))
            sleepLittle()
            adbshell.tap(getRandomNumber(578, 707), getRandomNumber(410, 460))
            sleepLittle()
            adbshell.tap(getRandomNumber(477, 701), getRandomNumber(600, 641))
            sleepLittle()
            adbshell.tap(getRandomNumber(581, 701), getRandomNumber(640, 641))
            sleepLittle()
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
            sleepLittle()
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
            sleepLong()
            continue

        playPoint = findpic.getLoc(src_img, "./img/zhandouzhunb.png")
        if playPoint:
            printThis("战斗失败之后的战斗准备")
            countFail += 1
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLong()
            continue

        playPoint = findpic.getLoc(src_img, "./img/shi.png")
        if playPoint:
            printThis("确定出售的  是 按钮")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue
        if (isGet):
            playPoint = findpic.getLoc(src_img, "./img/get.png")
            if playPoint:
                printThis("获得道具")
                adbshell.tap(playPoint[0], playPoint[1])
                sleepLittle()
                continue
        else:
            playPoint = findpic.getLoc(src_img, "./img/chushou1.png")
            if playPoint:
                printThis("出售")
                adbshell.tap(playPoint[0], playPoint[1])
                sleepLittle()
                continue

        playPoint = findpic.getLoc(src_img, "./img/sure.png")
        if playPoint:
            printThis("确认")
            adbshell.tap(playPoint[0], playPoint[1])
            sleepLittle()
            continue

        playPoint = findpic.getLoc(src_img, "./img/shengli.png")
        if playPoint:
            printThis("胜利")
            adbshell.tap(getRandomNumber(500, 600), getRandomNumber(60, 500))
            sleepLittle()
            adbshell.tap(getRandomNumber(500, 600), getRandomNumber(60, 500))
            sleepLittle()
            continue

        playPoint = findpic.getLoc(src_img, "./img/shibai.png")
        if playPoint:
            printThis("游戏失败 重开")
            adbshell.tap(getRandomNumber(700, 930), getRandomNumber(430, 500))
            sleepLittle()
            continue

        if (time.time() - game_begin_agein > out_time):
            exitPrint("游戏超时")

        printThis("随便点击一下")
        adbshell.tap(getRandomNumber(300, 800), getRandomNumber(600, 700))
        sleepLong()
        pass


tk = Tk()
tk.title("魔灵")
isBengin = False


# tk.geometry("400x400")
# tk.resizable(False, False)


def close():
    time.sleep(3)
    tk.quit()


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
    Button(fm, text="设置为默认火山地狱", command=clickHuoshan).pack(side=LEFT, fill=X, expand=NO)
    Button(fm, text="设置为默认巨人10", command=clickJuren).pack(side=LEFT, fill=X, expand=NO, padx=20)
    Button(fm, text="保存设置", command=clickSave).pack(side=LEFT, fill=X, expand=NO)
    fm.pack(side=TOP, fill=X, ipady=20, ipadx=20)

    btn_begin = Button(tk, text="开始", command=clickBegin, height=2)
    btn_begin.pack(side=TOP, fill=X, pady=8)
    btn_end = Button(tk, text="结束", command=clickEnd, height=2)
    btn_end.pack(side=TOP, fill=X)


def clickHuoshan():
    global isGet
    eSV1.set("45")
    isGet = False


def clickJuren():
    global isGet
    isGet = True
    eSV1.set("200")


def clickSave():
    global sleepTime, all, allMoney, out_time
    sleepTime = int(eSV1.get())
    allMoney = int(eSV2.get())
    all = int(eSV3.get())
    out_time = int(eSV4.get())


def clickBegin():
    global isBengin
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
    eSV1.set("200")
    eSV2.set("4")
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
