#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Lutz Engels <lutz.engels@os3.nl>

from ical_processing import iCalStream

# Specify ics-file
calfile = '/home/alboe/Desktop/LEITS.ics'
#calfile = '/home/alboe/sne/wiki/RP2/git-code/icalendar/src/icalendar/tests\
#           /issue_53_parsing_failure.ics'
# Create iCalStream instance
calstore = iCalStream()
# Load ics-file content into instance
calstore.read_ics(calfile)
# How many calendars does the file contain?
print calstore.calenderset.__len__()
# Print certain component
calstore.get_component('vevent')
# Print value of property only
#print calstore.calenderset[0]['uid']

# Address subcomponents
#activecal = calstore.calenderset[0]
#print activecal['prodid']
