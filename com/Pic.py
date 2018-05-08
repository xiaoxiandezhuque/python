import re
import time

from pip._vendor import requests

# text = "http://img06.tooopen.com/images/20160921/tooopen_sy_179583447187.jpg"
# reg = r"http://img.*?\.tooopen.com/images/.*?\.jpg"
# reg = r".*?t"
# b = re.findall(reg, text, re.S)
# print(b)

local = time.strftime("%Y%m%d")
url = r'http://www.tooopen.com/view/1280706.html'
con = requests.get(url)
content = con.text
reg = r"http://img.*?\.tooopen.com/images/.*?\.jpg"

a = re.findall(reg, content, re.S)[0]
print(a)

read = requests.get(a)
f = open('%s.jpg' % local, 'wb')
f.write(read.content)
f.close()
