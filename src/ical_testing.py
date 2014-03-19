#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Lutz Engels <lutz.engels@os3.nl>

from ical_processing import iCalStream

# Specify ics-file
calfile = 'icaltest.ics'
#calfile = '/home/alboe/sne/wiki/RP2/git-code/icalendar/src/icalendar/tests\
#           /issue_53_parsing_failure.ics'
# Create iCalStream instance
calstore = iCalStream()
# Load ics-file content into instance
calstore.read_ics(calfile)
# How many calendars does the file contain?
print "Nr of calendars in %s: %d" % (calfile, calstore.calendarset.__len__())
# Print certain component
print calstore.get_component('ALL', 'UID',
                             'a139435f-1c58-4492-a898-d69ca75f4746')
