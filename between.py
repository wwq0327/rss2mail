#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    between
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-11-01
    :author: wwq0327 <wwq0327@gmail.com>
    :license: LGPL 2 or later (see README/COPYING/LICENSE)

"""

from dateutil import rrule
import datetime

def weeks_between(start_date, end_date):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date)
    return weeks.count()

if __name__ == '__main__':
    starts = [datetime.date(2005, 01, 04), datetime.date(2005, 01, 03)]
    end = datetime.date(2005, 01, 10)
    for s in starts:
        days = rrule.rrule(rrule.DAILY, dtstart=s, until=end).count()
        print "%d days shows as %d weeks" % (days, weeks_between(s, end))
