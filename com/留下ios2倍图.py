import os

basePath = r"C:\Users\Administrator\Desktop\详情页图标"

index = 1


def renamefile(path):
    global index
    fileNames = os.listdir(path)
    # print(fileNames)
    for fileName in fileNames:
        if os.path.isdir(path + "\\" + fileName):
            renamefile(path + "\\" + fileName)
            pass
        elif (fileName.find(".png") != -1):
            if (fileName.find("@2x") != -1):
                # pass
                os.rename(path + "\\" + fileName, basePath + "\\" + fileName.replace("@2x", "%s" % (index)))
                index += 1;
            else:
                os.remove(path + "\\" + fileName)


if __name__ == "__main__":
    renamefile(basePath)
pass
