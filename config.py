#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    config
    ~~~~~~~~~~~~~~~~~~~~

    读取RSS的相关配置及邮件发送配置
    
    :date: 2011-11-01
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPL or later (see README/COPYING/LICENSE)

"""
# 日志地址列表, 可自行添加博客的RSS地址，暂只在wordpress日志系统上测试通过
BLOG_ADDR_LIST = ["http://sociallearnlab.org/xiuli/?feed=rss2",
                  "http://linuxtoy.org/?feed=rss2",
                  ]
             
# 读取日志的最大限制大数
MAX_DT_DAYS = 7 # 7, 表示读当前日期7天前的记录，含当前日期

# 邮件发送相关配置
