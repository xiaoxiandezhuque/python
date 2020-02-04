import requests
import random
import base64
from Crypto.Cipher import AES
import json

headers = {
    'User-Agent': 'okhttp/3.10.0',
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
    'Host': 'jk.q5oq1r7e.com',
    'Content-Type': 'application/x-www-form-urlencoded'}
session = requests.session()

key_bytes = bytes("xPxo2S5uGPhKHx5g", encoding='utf-8')
iv_bytes = bytes("0a1b2c3d4e5f6789", encoding='utf-8')

d = {"app": "1",
     "platform": "1",
     "k": "hyfr6iyPZMZfJFEc",
     "t": "14161320495989",
     "token": "",
     "version": "1.5.2",
     "versionapi": "1.5.0",
     "Connection": "close", }
loginurl = "https://jk.q5oq1r7e.com/api/bootstrap"


def getRandom():
    return random.randrange(13161320495989, 14161320495989)


# 字典排序
def sort(map):
    map1 = sorted(map)
    map2 = dict()
    for i in map1:
        map2[i] = map[i]
    return map2


def getdata(url):
    headers['']
    d = {"Connection": "close",
         "app": "1",
         "platform": "1",
         "k": "hyfr6iyPZMZfJFEc",
         "t": "14161320495989",
         "token": "",
         "version": "1.5.2",
         "versionapi": "1.5.0"}

    req = session.get(url, headers=headers)
    req.content.decode(req.encoding, "ignore").encode("utf-8", "ignore")


def encrypt(content):

    # cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    # 加密
    # encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    # 重新编码
    # result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    # return result
    pass

def decrypt(key, content):
    key_bytes = bytes(key, encoding='utf-8')
    iv = key_bytes
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # base64解码
    encrypt_bytes = base64.b64decode(content)
    # 解密
    decrypt_bytes = cipher.decrypt(encrypt_bytes)
    # 重新编码
    result = str(decrypt_bytes, encoding='utf-8')
    return result


if __name__ == '__main__':
    d["t"] = getRandom()
    myD = sort(d)
    print(myD)
    djson =json.dumps(myD)
    print(djson)
