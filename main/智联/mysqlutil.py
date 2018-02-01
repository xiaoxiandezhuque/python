#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
from pymysql import IntegrityError


def addDetailUrls(urls):
    try:
        conn = pymysql.connect(host='localhost', cursorclass=pymysql.cursors.DictCursor,
                               user='root', passwd=None, db='new_schema', charset='utf8mb4')
        cur = conn.cursor()
        sql = "INSERT INTO zhiliandetailurls(url) VALUES "
        if len(urls)>0:
            for url in urls:
                if url.startswith("http://jobs.zhaopin.com"):
                    sql = "%s ('%s')," % (sql, url)
        else:
            return
        postion = sql.rfind(',')
        sql = sql[0:postion]
        cur.execute(sql)
        conn.commit()
    except IntegrityError:
        # print(urls)
        print("重复")
        print("--------------")
    finally:
        cur.close()
        conn.close()


def getDetailUrls(start, end):
    try:
        conn = pymysql.connect(host='localhost', cursorclass=pymysql.cursors.DictCursor,
                               user='root', passwd=None, db='new_schema', charset='utf8mb4')
        cur = conn.cursor()
        sql = """ SELECT *
                    FROM (
                           SELECT
                             a.id url_id,
                             a.url,
                             b.title
                           FROM zhiliandetailurls a LEFT JOIN job b ON a.id = b.zl_id
                           ORDER BY a.id
                           LIMIT %s,%s
                         ) c
                    WHERE title is NULL""" % (start, end)
        cur.execute(sql)
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def saveDetail(dic_detail):
    try:
        conn = pymysql.connect(host='localhost', cursorclass=pymysql.cursors.DictCursor,
                               user='root', passwd=None, db='new_schema', charset='utf8mb4')
        cur = conn.cursor()
        sql = """INSERT INTO job(title,money,place,state,nature,
                         work_year,education,num_of_people,category,address,description,company_name,company_detail,
                          zl_id,company_people,company_nature,company_industry) VALUES ("%s", "%s", "%s", "%s", "%s", "%s",
                                 "%s", "%s", "%s", "%s", "%s",
                        "%s", "%s","%s","%s","%s","%s")""" % (dic_detail["title"],
                                                              dic_detail["money"],
                                                              dic_detail["place"],
                                                              dic_detail["state"],
                                                              dic_detail["nature"],
                                                              dic_detail["work_year"],
                                                              dic_detail["education"],
                                                              dic_detail["num_of_people"],
                                                              dic_detail["category"],
                                                              dic_detail["address"],
                                                              dic_detail["description"],
                                                              dic_detail["company_name"],
                                                              dic_detail["company_detail"],
                                                              dic_detail['zl_id'],
                                                              dic_detail['company_people'],
                                                              dic_detail['company_nature'],
                                                              dic_detail['company_industry'])

        cur.execute(sql)
        conn.commit()
    except IntegrityError:
        # print(urls)
        print("重复")
        print("--------------")
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    # getDetailUrls(0, 10)
    try:
        conn = pymysql.connect(host='localhost', cursorclass=pymysql.cursors.DictCursor,
                               user='root', passwd=None, db='new_schema', charset='utf8mb4')
        cur = conn.cursor()
        sql = """ SELECT *
                    FROM (
                           SELECT
                             a.id ulr_id,
                             a.url,
                             b.title
                           FROM zhiliandetailurls a LEFT JOIN job b ON a.id = b.zl_id
                           ORDER BY a.id
                           LIMIT 10
                         ) c
                    WHERE title is NULL"""
        cur.execute(sql)
        print(cur.fetchall())

    finally:
        cur.close()
        conn.close()
