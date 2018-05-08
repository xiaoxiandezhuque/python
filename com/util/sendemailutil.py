#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class sendemail:

    def send(self, title, fromWhere, toWhere, content):
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['Subject'] = Header(title, 'utf-8').encode()
        msg['From'] = Header(fromWhere, 'utf-8').encode()
        msg['To'] = Header(toWhere).encode()
        try:
            smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
            smtp.login(r'962139864@qq.com', r'')
            smtp.sendmail('962139864@qq.com', ['962139864@qq.com', ], msg.as_string())
        except smtplib.SMTPException:
            print("失败")
            raise
            # smtplib.SMTPException.
        finally:
            smtp.quit()


if  __name__ == "__main__":
    sendemail().send("aaa","aa",'aa','aaaaa')
    print('---------------------')