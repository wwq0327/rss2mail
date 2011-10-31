#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    rss2mail
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-10-31
    :author: wwq0327 <wwq0327@gmail.com>
    :license: LGPL 2 or later (see README/COPYING/LICENSE)

"""

import feedparser

blog_addr = "http://sociallearnlab.org/xiuli/?feed=rss2"

def read_blog(entries):
    da_list = []

    blog_info = {}
    if entries:
        blog_info['title'] = entries.title

        da_list.append(blog_info)

    return da_list

def main():
    d = feedparser.parse(blog_addr)

    for i in xrange(2):
        entries = d.entries[i]
        result = read_blog(entries)

        print result

if __name__ == '__main__':
    main()
