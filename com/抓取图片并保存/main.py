import requests
from lxml import etree
import re
from http import cookiejar
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://m.applwx.cn/wap/read/view/id/91/cpid/1591/t/2054', }
session = requests.session()
cookies = {'PHPSESSID': 'jcs2490mp57sionve2dbkegaj1', 'yw_reaua': '5T96928297',
           'yw_reauapwd': '308a669a908b83b4279de19d60069c72', 'reauacid': '0',
           'yw_user_ip': '3206ade6f6169873194db95bb88f9008'}


def getHtml(url):
    req = session.get(url, headers=headers)
    req.content.decode(req.encoding, "ignore").encode("utf-8", "ignore")
    result = etree.HTML(req.content)
    print(result)
    return result


if __name__ == "__main__":
    # getHtml("https://www.baidu.com/")
    # http://www.zhlzw.com/UploadFiles/Article_UploadFiles/201204/20120412123923816.jpg
    # http://wapled.cn/images/91/1591/Compress_1%20(1).jpg?2018092012131312
    num = 901
    page = 1
    duoshaohua = 10
    while True:
        # url = "http://wapled.cn/images/80/1188/Compress_1%20(%s).jpg?2018092012131312" % (num, page)
        url = 'http://wapled.cn/images/60/' + str(num) + '/Compress_1%20(' + str(page) + ').jpg?2018092012131312'

        html = session.get(url,
                           headers=headers)
        if (page == 1 and not os.path.exists("./%s话" % duoshaohua)):
            # os.makedirs("./%s话" % (num - 1187))
            os.makedirs("./%s话" % duoshaohua)
        if (html.status_code == 200):
            with open('./%s话/%s页.jpg' % (duoshaohua, page), 'wb') as file:
                file.write(html.content)
                file.close()
                page += 1
        else:
            # if(num==1197):
            exit()
            # num += 1
            # page = 1

pass
