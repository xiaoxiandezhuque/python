import os
import threading
import time


def print11():
    while True:
        print("1111")
        time.sleep(2)


def print22():
    while True:
        print("22222")
        time.sleep(2)


t = threading.Thread(target=print11)
# t.setDaemon(True)
t.start()

# print22()
t.join()