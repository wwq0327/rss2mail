#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    rss2mail
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-10-31
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPL or later (see README/COPYING/LICENSE)

"""
import datetime
import feedparser
from dateutil import parser, rrule

MAX_DAYS = 7
blog_addr = "http://sociallearnlab.org/xiuli/?feed=rss2"

def rss_parser(rssaddr):
    """返回解析对象

    :param rssaddr: 博客的RSS地址

    """
    
    return feedparser.parse(rssaddr)

def read_blog(entries):
    """读取一条日志, 返回字典：
    
    :title: 标题
    :updated: 更新日期
    :link: 日志链接地址
    :content: 内容，只取了140个字符。
    """

    blog_info = {}
    if entries:
        blog_info['title'] = entries.title
        blog_info['updated'] = entries.updated
        blog_info['link'] = entries.link
        blog_info['content'] = entries.summary[0:140]

    return blog_info

def store_recoder(blog):
    """读取单条RSS信息内容，并与限定时间进行比较。
    """
    
    updated = blog['updated']
    blog_time = parser.parse(updated) ## 解析日期
    my_d = blog_time.strftime("%Y-%m-%d %H")
    my_time = datetime.datetime.strptime(my_d, "%Y-%m-%d %H") ## 转换成rrule可读日期对象
    
    td_now = datetime.datetime.now()

    days = rrule.rrule(rrule.DAILY, dtstart=my_time, until=td_now).count() ## 获取RSS日期与当前日期所差天数 

    if 0 <= days <= MAX_DAYS:
        return True
    else:
        return False

def feed(d):
    dict_list = []

    for i in xrange(10):
        entries = d.entries[i]
        result = read_blog(entries)
        rss = store_recoder(result)

        if rss:
            dict_list.append(result)

    return dict_list

def main():
    
    rss = rss_parser(blog_addr)
    dict_list = feed(rss)

    for d in dict_list:
        print d['title'], d['link'], d['updated']

if __name__ == '__main__':
    main()
