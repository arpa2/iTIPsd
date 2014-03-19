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

    def __init__(self, *args, **kwargs):
        """Set keys initial stream properties.
        """
        self.username = self._get_username()

    def __iter__(self):
        """Returns iterable component list
        """
        return iter(self.calendarset)

    def read_ics(self, filepath):
        """Parse .ics file and add calendar objects to list.
        """
        #TODO# raise error if file doesn't exist
        # Parse .ics file
        icsfile = open(filepath, 'rb')
        self.calendarset = Calendar.from_ical(  # create list-object
            icsfile.read(),
            multiple=True
        )
        #debug#print self.calendarset
        #debug#print type(self.calendarset)
        icsfile.close

    def raw_data(self):
        """
        """
        self.walk()

    def _recurse_component(self, component):
        """
        """
        result = []
        if component is None or component == "VERSION":
            print "Got a match!"
            result.append(component)
        for subcomponent in component:
            print subcomponent
        return result

    def get_component(self, comp, prop, searchterm):
        """Returns list of requested Component object
        """
        component_matches = []
        #TODO Check if comp is valid
        for cal in self.calendarset:
            print cal.name
            for component in cal.subcomponents:
                print component.name

               #TODO hardcoded exclusion (not in), not so nice, use some other
               #TODO reference, pls
                if component.name == comp or (comp == 'ALL' and component.name
                   not in ['VTIMEZONE', 'VALARM']):
                    #print "Yippie!"
                    #print component[prop]
                    if component.has_key(prop):
                        if component[prop] == searchterm:
                            print "Matched! ",
                            print "%s>%s:%s" % (cal.name, component.name,
                                                component[prop])
                            # Add match to list
                            component_matches.append(component)
        return component_matches

    def _get_username(self):
        """Return username as extracted from the file path.
        """
        #TODO# strip user from file-path
        result = 'www-data'
        return result

    #TODO# def get_all_the_nice_sub_components_and_parameters():
