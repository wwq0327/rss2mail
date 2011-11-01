#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    rss2html
    ~~~~~~~~~~~~~~~~~~~~

    RSS To HTML
    
    :date: 2011-11-01
    :author: wwq0327 <wwq0327@gmail.com>
    :license: LGPL 2 or later (see README/COPYING/LICENSE)

"""

import blogrssparser

BLOG_ADDR = 'http://linuxtoy.org/?feed=rss2'

HTML_HEAD = """
<!DOCTYPE html>
<html><head><title>RSS To HTML</title><head><body>
<h1>RSS To HTML</h1>
"""

HTML_END = "</body></html>"

def get_rss_list(addr):
    r = blogrssparser.BlogRSS(addr)
    d = r.blog_parser()

    return r.feed(d)

def rss2html():
    rss_list = get_rss_list(BLOG_ADDR)
    print HTML_HEAD

    print "<ul>"
    for d in rss_list:
        print """<li><a href=%s>%s</a> Updated: %s<br />
        %s <br /></li>""" % (d['link'], d['title'], d['updated'], d['content'])

    print "</ul>"

    print HTML_END

if __name__ == '__main__':
    rss2html()
        

    
