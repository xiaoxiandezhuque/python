import autopy
from autopy.mouse import Button
import time
import random
from com.pc import config


def movePoint(replacePoint, beginX, beginY):
    # print("移动点（%s，%s）到（%s，%s），颜色是%s"
    #       % (replacePoint.fromPoint.x, replacePoint.fromPoint.y, replacePoint.toPoint.x, replacePoint.toPoint.y,
    #          replacePoint.color))

    autopy.mouse.smooth_move(beginX + replacePoint.fromPoint.x * config.get_bead_width() + random.randrange(10, 40),
                             beginY + replacePoint.fromPoint.y * config.get_bead_width() + random.randrange(10, 40))
    autopy.mouse.toggle(Button.LEFT, True)
    time.sleep(random.randrange(300, 1000) / 1000)
    autopy.mouse.smooth_move(beginX + replacePoint.toPoint.x * config.get_bead_width() + random.randrange(10, 40),
                             beginY + replacePoint.toPoint.y * config.get_bead_width() + random.randrange(10, 40))
    time.sleep(random.randrange(100, 300) / 1000)
    autopy.mouse.toggle(Button.LEFT, False)
    pass

def downPoint(point):
    autopy.mouse.smooth_move(point[0], point[1])
    autopy.mouse.toggle(Button.LEFT, True)
    time.sleep(random.randrange(100, 300) / 1000)
    autopy.mouse.toggle(Button.LEFT, False)

