import copy


# 转换一种颜色
def colorTransition(beadList, fromColor, toColor):
    list = copy.deepcopy(beadList)
    for i in range(8):
        for j in range(8):
            if list[i][j] == fromColor:
                list[i][j] = toColor
    return list


# 转换一种颜色
def color2Transition(beadList, fromColor1, toColor1, fromColor2, toColor2):
    list = copy.deepcopy(beadList)
    for i in range(8):
        for j in range(8):
            if list[i][j] == fromColor1:
                list[i][j] = toColor1
            elif list[i][j] == fromColor2:
                list[i][j] = toColor2
    return list
