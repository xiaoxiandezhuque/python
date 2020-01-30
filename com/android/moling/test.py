import os
import threading
import time

machine = os.popen("adb devices")
machineStr = machine.read()
print(machineStr)


