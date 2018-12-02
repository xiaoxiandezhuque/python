from com.android import findpic
from com.android import adbshell
from com.android.moling import myUtils


class PlayLong:

    def __init__(self, src_img):
        self.src_img = src_img

    def begin(self):


        pass

    def isGetGoods(self):
        playPoint = findpic.getLoc(self.src_img, "./img/get.png")
        if playPoint:
            print("获取道具")
            adbshell.tap(playPoint[0], playPoint[1])
            myUtils.sleepLittle()
            return True
