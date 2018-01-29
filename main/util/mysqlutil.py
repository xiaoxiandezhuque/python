#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import time
import pymysql


class mysqlutil:

    def getUrlBean(self):
        try:
            conn = pymysql.connect(host='localhost', cursorclass=pymysql.cursors.DictCursor,
                                   user='root', passwd=None, db='new_schema', charset='utf8mb4')
            cur = conn.cursor()
            sql = "SELECT * FROM xiaoshuo"

            cur.execute(sql)
            return cur.fetchall()
        finally:
            cur.close()
            conn.close()

    def updataAddress(self, id, newValue):
        try:
            conn = pymysql.connect(host='localhost', cursorclass=pymysql.cursors.DictCursor,
                                   user='root', passwd=None, db='new_schema', charset='utf8mb4')
            cur = conn.cursor()
            sql = """UPDATE xiaoshuo
                SET newAddress = "%s"
                WHERE id = %s""" % (newValue, id)
            cur.execute(sql)
            conn.commit()
        finally:
            cur.close()
            conn.close()
