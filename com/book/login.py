#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

params = {"username": "haha", "password": "password"}

r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("cookie is  set to : %s", r.cookies.get_dict())
print("-----------------")
print("Going to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",
                 cookies=r.cookies)
print(r.text)
