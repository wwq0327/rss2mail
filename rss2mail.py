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

blog_addr = "http://sociallearnlab.org/xiuli/?feed=rss2"

def read_blog(entries):
    '''读取一条日志'''

    blog_info = {}
    if entries:
        blog_info['title'] = entries.title
        blog_info['updated'] = entries.updated
        blog_info['link'] = entries.link
        blog_info['content'] = entries.summary[0:140]

    return blog_info

def store_recoder(blog):
    """读取单条RSS信息内容，并与限定时间进行比较，
    如果在限定时间范围之类，则输出。
    """
    updated_time = blog['updated']
    blog_time = parser.parse(updated_time)
    my_d = blog_time.strftime("%Y-%m-%d %H")
    my_time = datetime.datetime.strptime(my_d, "%Y-%m-%d %H")
    
    td_now = datetime.datetime.now()

    days = rrule.rrule(rrule.DAILY, dtstart=my_time, until=td_now).count()

    if 0 <= days <= 7:
        return True
    else:
        return False

def main():
    dict_list = []
    d = feedparser.parse(blog_addr)
    
    ## 读取博客的前十条RSS
    for i in xrange(10):
        entries = d.entries[i]
        result = read_blog(entries)
        rss = store_recoder(result)
        if rss:
            dict_list.append(result)

    for d in dict_list:
        print d['title'], d['link'], d['updated']

if __name__ == '__main__':
    main()
