import os

if __name__ == "__main__":
    filePath = r"E:\work\waibao_wuliu\ui\报事详情\报事详情页切图"
    fileNames = os.listdir(filePath)
    print(fileNames)
    for file in fileNames:

        if (file.find(".png") != -1):
            if (file.find("@2x") != -1):
                # pass
                os.rename(filePath + "\\" + file, filePath + "\\" + file.replace("@2x", ""))
            else:
                os.remove(filePath + "\\" + file)
