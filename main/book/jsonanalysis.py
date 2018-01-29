#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from urllib.request import urlopen
from urllib.request import urlretrieve


def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
   # json解析
    responseJson = json.loads(response)
    print(responseJson)
    return responseJson.get('country_code')

# 下载文件
def download():
    urlretrieve("url","filename")



print(getCountry("50.78.253.58"))
