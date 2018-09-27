import requests
from lxml import etree
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', }
session = requests.session()


def getHtml(url):
    req = session.get(url, headers=headers)
    req.content.decode(req.encoding, "ignore").encode("utf-8", "ignore")
    result = etree.HTML(req.content)
    print(result)
    return result


if __name__ == "__main__":
    getHtml("https://www.baidu.com/")

    html = requests.get(
        'http://www.zhlzw.com/UploadFiles/Article_UploadFiles/201204/20120412123923816.jpg')
    with open('picture.jpg', 'wb') as file:
        file.write(html.content)

pass
