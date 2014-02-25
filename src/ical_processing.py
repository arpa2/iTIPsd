#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Lutz Engels <lutz.engels@os3.nl>
"""
Pseudocode:

read file.ics
count e.g. number of $parameter
check if compliant
if not print $parameter and conflict
"""

from icalendar import Calendar
#import os


class iCalStream(object):
    """Object containing a set of iCalender objects
    """
    username = ''
    calenderset = {}  # Will store Calender objects

    def __init__(self, *args, **kwargs):
        """Set keys initial stream properties.
        """
        self.username = self._get_username()

    def read_ics(self, filepath):
        """Parse .ics file and add calendar objects to list.
        """
        #TODO# raise error if file doesn't exist
        # Parse .ics file
        icsfile = open(filepath, 'rb')
        self.calenderset = Calendar.from_ical(  # create list-object
            icsfile.read(),
            multiple=True
        )
        icsfile.close

    def raw_data(self):
        """
        """
        self.walk()

    def _recurse_component(self, component):
        """
        """
        for subcomponent in component:
            print subcomponent
            print "Infinite recursion in line 52"
#            self._recurse_component(subcomponent)

    def get_component(self, comp):
        """Returns requested Component object
        """
        #TODO# create component-object, fill it, return it
        for cal in self.calenderset:
            self._recurse_component(cal)
        #    print cal.name
        #    #print cal.walk()
        #    for component in cal:
#                print component
        #        print "\t" + component, self.calenderset[0][component]
#            for subcomp in cal.subcomponents:
#                for lol in subcomp:
#                    print lol
        #        print subcomp.walk(comp)
#        return self._getcomponent(comp)

    def _get_username(self):
        """Return username as extracted from the file path.
        """
        #TODO# strip user from file-path
        result = 'www-data'
        return result

    #TODO# def get_all_the_nice_sub_components_and_parameters():
