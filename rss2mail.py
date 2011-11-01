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
    ## da_list = []

    blog_info = {}
    if entries:
        blog_info['title'] = entries.title
        blog_info['updated'] = entries.updated
        blog_info['link'] = entries.link
        blog_info['content'] = entries.summary[0:140]

    return blog_info

def store_recoder(blog):
    updated_time = blog['updated']
    #print updated_time
    blog_time = parser.parse(updated_time)
    my_d = blog_time.strftime("%Y-%m-%d %H")
    my_time = datetime.datetime.strptime(my_d, "%Y-%m-%d %H")
    
    td_now = datetime.datetime.now()

    days = rrule.rrule(rrule.DAILY, dtstart=my_time, until=td_now).count()
    #print days

    if 0 <= days <= 10:
        print blog['title']
    else:
        print '无记录'

def main():
    d = feedparser.parse(blog_addr)

    for i in xrange(10):
        entries = d.entries[i]
        result = read_blog(entries)

        store_recoder(result)

        #print result

if __name__ == '__main__':
    main()
