#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    rss2mail
    ~~~~~~~~~~~~~~~~~~~~

    将信息发送到邮件

    :参考: http://zsp.iteye.com/blog/248484
    
    :date: 2011-11-01
    :author: wwq0327 <wwq0327@gmail.com>
    :license: LGPL 2 or later (see README/COPYING/LICENSE)

"""
import sys
from email.mime.text import MIMEText
import smtplib

import config

class ToGmail(object):
    """将收集到的信息打包发送到Gmail"""

    def __init__(self, account, password):
        """ToGmail("USERNAME@gmail.com", "PASSWORD")

        :param account: 邮箱帐号，包含"@gmail.com"部份
        :param password: 密码

        """

        self.account = account
        self.password = password

    def send(self, to, title, content):
        """发送邮件到接收人

        :param to: 邮件接收者。
        :param title: 邮件标题
        :param content: 邮件内容

        """

        server = smtplib.SMTP(config.MAIL_SERVER)
        server.docmd("EHLO server")
        server.starttls()
        server.login(self.account, self.password)

        msg = MIMEText(content)
        msg['Content-Type'] = 'text/plain; charset="utf-8"'
        msg['Subject'] = title
        msg['From'] = self.account
        msg['To'] = to
        server.sendmail(self.account, to, msg.as_string())
        server.close()

if __name__ == "__main__":
    passwd = raw_input("Gmail Password:").split()
    account = config.MAIL_ACCOUNT
    gmail = ToGmail(account, passwd)
    gmail.send(account, "hello, world", 'test')
