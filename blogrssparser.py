#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    blogrssparser
    ~~~~~~~~~~~~~~~~~~~~

    Blog RSS 解析类，以此类解析后，生成一个由字典组织的列表
    暂时只支持Wordpress RSS。
    
    :date: 2011-11-01
    :author: wwq0327 <wwq0327@gmail.com>
    :license: LGPL 2 or later (see README/COPYING/LICENSE)

"""

import datetime
import feedparser
from dateutil import parser, rrule

import config

class BlogRSS(object):
    def __init__(self, addr):
        """初始化

        :param addr: Blog RSS地址

        """

        self.addr = addr
        self.rss_info = {}
        self.dict_list = []

    def blog_parser(self):
        """返回解析对象"""

        return feedparser.parse(self.addr)

    def parser_rss(self, entries):
        """记录一条日志，返回字典"""

        if entries:
            self.rss_info['title'] = entries.title  ## 标题
            self.rss_info['updated'] = entries.updated  ## 发布日期
            self.rss_info['link'] = entries.link  ## 文章链接
            self.rss_info['content'] = entries.summary[0:140]  ## 日志内容，取前140个字符

        return self.rss_info

    def get_rss(self, rss):
        """读取单条RSS信息内容，并与限并时间进行比较。
        """

        updated = rss['updated']
        entries_time = parser.parse(updated) ## 解析日期，很强大
        my_d = entries_time.strftime("%Y-%m-%d %H")
        my_time = datetime.datetime.strptime(my_d,
                                             "%Y-%m-%d %H")
        # 获到当时时间
        td_now = datetime.datetime.now()

        # 所读取日期与当前时间相差天数
        days = rrule.rrule(rrule.DAILY,
                           dtstart=my_time,
                           until=td_now).count()

        if 0 <= days <= config.MAX_DT_DAYS:
            return True
        else:
            return False

    def feed(self, d):
        """获到单个博客限定范围内的RSS"""

        for i in xrange(10):
            entries = d.entries[i]
            result = self.parser_rss(entries)
            rss = self.get_rss(result)

            if rss:
                self.dict_list.append(result)

        return self.dict_list

def main():
    r = BlogRSS('http://linuxtoy.org/?feed=rss2')
    d = r.blog_parser()
    rss_dict = r.feed(d)
    print rss_dict

if __name__ == '__main__':
    main()
    
    
