import os

if __name__ == '__main__':
    os.system("adb shell screencap -p /sdcard/z_pic.png")
    os.system(r"adb pull /sdcard/z_pic.png E:\work\python\main\android")
