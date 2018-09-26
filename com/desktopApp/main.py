from tkinter import *
from tkinter import ttk
import time
import threading
import os
import random
import time



tk = Tk()
tk.title("魔灵")
isBengin = False


# tk.geometry("400x400")
# tk.resizable(False, False)


def close():
    time.sleep(3)
    tk.quit()


def createLabelAndEntry(labelText):
    fm = Frame(tk, bg="white", padx=15, pady=8)
    Label(fm, text=labelText, bg="white", width=20).pack(side=LEFT)
    e = StringVar()
    Entry(fm, textvariable=e, width=20).pack(side=LEFT, fill=X, expand=YES)
    fm.pack(side=TOP, fill=X)
    return e


def createLabel(fm):
    label = Label(fm, text="", bg="white", width=20, height=10, justify=LEFT)
    label.pack(side=LEFT, expand=NO)
    return label


def setLabelText(okCount, failCount, bugCount):
    label['text'] = "总次数:　　　　%s\n失败次数:　　　%s\n购买体力次数:　%s\n上次记录时间:　%s\n" \
                    % (okCount, failCount, bugCount, time.strftime("%H:%M:%S"))


def createList(fm):
    lb = Listbox(fm, width=20, height=10)
    lb.pack(side=LEFT)
    sl = ttk.Scrollbar(fm)
    sl.pack(side=LEFT, fill=Y)
    sl['command'] = lb.yview
    return lb


def crtateBtn():
    global btn_begin, btn_end
    fm = Frame(tk, bg="white")
    btn_huoshan = Button(fm, text="设置为默认火山地狱", command=clickHuoshan).pack(side=LEFT, fill=X, expand=NO)
    btn_juren = Button(fm, text="设置为默认巨人10", command=clickJuren).pack(side=LEFT, fill=X, expand=NO, padx=20)
    fm.pack(side=TOP, fill=X, ipady=20, ipadx=20)

    btn_begin = Button(tk, text="开始", command=clickBegin, height=2)
    btn_begin.pack(side=TOP, fill=X, pady=8)
    btn_end = Button(tk, text="结束", command=clickEnd, height=2)
    btn_end.pack(side=TOP, fill=X)


def clickHuoshan():
    eSV1.set("45")


def clickJuren():
    eSV1.set("220")


def clickBegin():
    global isBengin
    if (eSV1.get() and eSV2.get() and eSV3.get() and eSV4.get()):
        lb.delete(0, END)  # 清空列表
        isBengin = True
        setLabelText(0, 0, 0)
        btn_begin['bg'] = "red"
        btn_end['bg'] = "white"
        print("you ")
    else:
        print("meiyou ")


def clickEnd():
    global isBengin
    isBengin = False
    btn_begin['bg'] = "white"
    btn_end['bg'] = "red"
    pass


def setDefult():
    eSV1.set("220")
    eSV2.set("4")
    eSV3.set("220")
    eSV4.set("900")
    setLabelText(0, 0, 0)


eSV1 = createLabelAndEntry("沉睡时间")
eSV2 = createLabelAndEntry("购买体力次数")
eSV3 = createLabelAndEntry("重复的最大次数")
eSV4 = createLabelAndEntry("超时时间")

fmLabel = Frame(tk, bg="white", padx=15, pady=8)
label = createLabel(fmLabel)
lb = createList(fmLabel)
fmLabel.pack(side=TOP, fill=X)

crtateBtn()

setDefult()

# Label(app, text=e.get(), bg="white").pack(side=LEFT)
# canvas = Canvas(tk, width=400, height=400, bg='white')
# canvas.pack()
# crtateBtn(tk)

# b = Button(tk,Text ="ok",COMMAND=callback())
# btn_juren = Button(tk, text="巨人10", command=callback).pack(side=TOP, anchor=W, fill=X, expand=NO)
# # btn_huoshan = Button(tk, text="火山地狱", command=callback).pack()

# t = threading.Thread(target=close)
# t.start()
tk.mainloop()

