import copy


# 看看是否可以转换一种颜色
def isCanUseColorTransition(beadList, fromColor, toColor):
    list = copy.deepcopy(beadList)
    for i in range(8):
        for j in range(8):
            if list[i][j] == fromColor:
                list[i][j] = toColor
    return find4(list)


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


def find4(beadList):
    for i in range(8):
        for j in range(8):
            color = beadList[i][j]
            count = 0
            # 找左右
            for c in range(1, 4):
                if i - c >= 0 and beadList[i - c][j] == color:
                    count += 1
                else:
                    break
            for c in range(1, 4):
                if i + c <= 7 and beadList[i + c][j] == color:
                    count += 1
                else:
                    break
            if count >= 3:
                return True

            # 找上下
            count = 0
            for c in range(1, 4):
                if j - c >= 0 and beadList[i][j - c] == color:
                    count += 1
                else:
                    break
            for c in range(1, 4):
                if j + c <= 7 and beadList[i][j + c] == color:
                    count += 1
                else:
                    break
            if count >= 3:
                return True

# def findcount(color,i,j,beadList):
# def findyi(color,i,j,beadList):
#     if i-1>=0 and beadList[i-1][j] == color:
#         return True
#
