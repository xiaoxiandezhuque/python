import frida;
import sys;

rdev = frida.get_remote_device()
session = rdev.attach("com.qiyi.video")

str = open("aiqiyi.js", 'r', encoding='UTF-8').read()

script = session.create_script(str)


def on_messgae(message, data):
    print(message)


script.on("message", on_messgae)
script.load()
sys.stdin.read()
