from com.android import findpic
from com.android import adbshell
from com.android.moling import myUtils


def takeFirst(pt):
    return pt[0]


class PlayGouLiang:

    def __init__(self, src_img):
        self.src_img = src_img

    # 42  455     822 522
    def begin(self):
        playPoint = findpic.getLoc(self.src_img, "./img/meiyoushangmoling.png")
        if playPoint:

            xingList = findpic.getAllLoc(self.src_img, "./img/xing3.png")
            if (xingList):
                dengjiList1 = findpic.getAllLoc(self.src_img, "./img/dengji1.png")
                dengjiList1 = self.cleandengji(dengjiList1)
                print(xingList)
                print(dengjiList1)

                zhaodao = set()
                for xing in xingList:
                    for dengji in dengjiList1:
                        juli = dengji[0] - xing[0]
                        if juli < 100 and juli > 0:
                            zhaodao.add((xing[0], xing[1]))
                            break
                        # else:

                print(zhaodao)
            # # 狗粮列表向左滑动
            # adbshell.swipe(myUtils.getRandomNumber(750, 822), myUtils.getRandomNumber(455, 522),
            #                myUtils.getRandomNumber(42, 60), myUtils.getRandomNumber(455, 522))
            # myUtils.sleepLittle()
            # adbshell.swipe(myUtils.getRandomNumber(750, 822), myUtils.getRandomNumber(455, 522),
            #                myUtils.getRandomNumber(42, 60), myUtils.getRandomNumber(455, 522))
            # print("带狗粮查看有没有上狗粮")
            # adbshell.tap(playPoint[0], playPoint[1])
            # myUtils.sleepLittle()

        pass

    def isGetGoods(self):
        playPoint = findpic.getLoc(self.src_img, "./img/chushou1.png")
        if playPoint:
            print("出售")
            adbshell.tap(playPoint[0], playPoint[1])
            myUtils.sleepLittle()
            return True

    # 22 440  867 546
    def cleandengji(self, dengjiList):
        chaochuSet = set()
        for dengji in dengjiList:
            if dengji[0] > 867 or dengji[0] < 160 or dengji[1] > 556 or dengji[1] < 435:
                chaochuSet.add(dengji)

        a = set(dengjiList)
        a -= chaochuSet
        b = list(a)
        b.sort(key=takeFirst)
        return b
        # return dengjiSet


if __name__ == "__main__":
    playWay = PlayGouLiang("./img/12.png")
    playWay.begin()
