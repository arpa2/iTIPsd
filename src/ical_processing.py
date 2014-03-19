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


class iCalStream(object):
    """Object containing a set of iCalender objects
    """
    username = ''

    def __init__(self, *args, **kwargs):
        """Set keys initial stream properties.
        """
        self.username = self._get_username()

#    def __iter__(self):
#        """Returns iterable component list
#        """
#        return iter(self.calendarset)

    def read_ics(self, filepath):
        """Parse .ics file and fill iCalStream with calender objects.
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

    def get_component(self, comp, prop, searchterm):
        """Returns list of requested Component object
        """
        matching_components = []
        #TODO Check if comp is valid
        for cal in self.calendarset:
            print cal.name
            for component in cal.subcomponents:
                print component.name

               #TODO hardcoded exclusion (not in), not so nice, use some other
               #TODO reference, pls
                if component.name == comp or (comp == 'ALL' and component.name
                   not in ['VTIMEZONE', 'VALARM']):
                    if component.has_key(prop):
                        if component[prop] == searchterm:
                            print "Matched! ",
                            print "%s>%s:%s" % (cal.name, component.name,
                                                component[prop])
                            # Add match to list
                            matching_components.append(component)
        return matching_components

    def _get_username(self):
        """Return username as extracted from the file path.
        """
        #TODO# strip user from file-path
        result = 'www-data'
        return result

    #TODO# def get_all_the_nice_sub_components_and_parameters():
