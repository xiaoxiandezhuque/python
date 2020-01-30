from com.android import findpic
from com.android.molingchushi import adbshell
from com.android.molingchushi import myUtils
from com.android.molingchushi.Game import Game

# 0 在桌面打开游戏  1 在游戏内的首页   2。打怪中
gamestate = 0

port = "62025"
src_img = r"C:\Users\Administrator\Nox_share\Image\%s.png" % port



if __name__ == "__main__":
    myUtils.saveScreenshot("62025", "62025.png")
    game = Game(src_img,port)
    game.starGame()


    pass
