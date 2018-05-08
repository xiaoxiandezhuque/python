#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

conn = pymysql.connect(host='localhost', cursorclass=pymysql.cursors.DictCursor,
                       user='root', passwd=None, db='new_schema', charset='utf8mb4', )
cur = conn.cursor()
# cur.execute('USE scraping')
cur.execute('SELECT * FROM USER WHERE  id=1')
print(cur.fetchone())

cur.close()
conn.close()
