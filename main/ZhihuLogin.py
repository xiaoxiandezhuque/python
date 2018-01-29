import requests, time

url = 'https://www.zhihu.com/#signin'


def get_captcha(data):
    with open('captcha.gif', 'wb') as fb:
        fb.write(data)
    return input('captcha')


def login(userName, password, onCaptcha):
    sessiona = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
