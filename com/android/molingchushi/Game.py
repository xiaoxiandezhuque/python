from com.android import findpic
from com.android.molingchushi import adbshell
from com.android.molingchushi import myUtils


class Game:

    def __init__(self, src_img, port):
        self.src_img = src_img
        self.port = port

#进入游戏，到主界面
    def starGame(self):
        playPoint = findpic.getLoc(self.src_img, "./img/img1.png")
        if playPoint:
            print("")
            adbshell.tap(self.port, playPoint[0], playPoint[1])
            myUtils.sleepLittle()

    # def
