#!/usr/bin/python
#
# Author: Lutz Engels <lutz.engels@os3.nl>
import parameter
import value

# superclass
class Property(object):
    """
    """

    name = ""
    valuetype = ()# one from Value subclass
    #NO# Those are defined in Component subclasses already:
    #required_only_once = () # PRODID, VERSION, V*-component
    #optional_only_once = ()
    #optional_multiple_times = ()
    
    #TODO# Might have to use implement these properties too
    #TODO# http://tools.ietf.org/search/rfc5545#section-3.5:
    #TODO# content-line notation
    #TODO# no ordering
    #TODO# case insensitive


    def __init__(self, *args, **kwargs):
        """
        """
        #TODO#
        pass



# subclasses
# reflects http://tools.ietf.org/search/rfc5545#section-8.3.2
#TODO# Since they are a lot, maybe put them in separate files like they are
#TODO# separated in prop.py of icalendar
#TODO# OR make different superclasses e.g. DateAndTimeComponetProperty,
#TODO# AlarmComponentProperty, etc
class Calscale(Property):
    """ RFC 5545: Calendar Scale 
    """
    name = 'CALSCALE'
    valuetype = value.Text()

class Method(Property):
    """ RFC 5545: Method
    """
    name = 'METHOD'
    valuetype = value.Text()

class Prodid(Property):
    """ RFC 5545: Product Identifier
    """
    name = 'PRODID'
    valuetype = value.Text()

class Version(Property):
    """ RFC 5545: Version 
    """
    name = 'VERSION'
    valuetype = value.Text()

class Attach(Property):
    """ RFC 5545: Attachment
    """
    name = 'ATTACH'
    valuetype = value.Uri()

class Categories(Property):
    """ RFC 5545: Categories
    """
    name = 'CATEGORIES'
    valuetype = value.Text()

class Class(Property):
    """ RFC 5545: Classification
    """
    name = 'CLASS'
    valuetype = value.Text()

class Comment(Property):
    """ RFC 5545: Comment
    """
    name = 'COMMENT'
    valuetype = value.Text()

class Description(Property):
    """ RFC 5545: Description 
    """
    name = 'DESCRIPTION'
    valuetype = value.Text()

class Geo(Property):
    """ RFC 5545: Geographic Position 
    """
    name = 'GEO'
    valuetype = value.Geo() # RFC says float, but it's special -> own type

class Location(Property):
    """ RFC 5545: Location
    """
    name = 'LOCATION'
    valuetype = value.Text()

class PercentComplete(Property):
    """ RFC 5545: Percent Complete
    """
    name = 'PERCENT-COMPLETE'
    valuetype = value.Integer() #???# Don't know if separate type is necessary

class Priority(Property):
    """ RFC 5545: Priority 
    """
    name = 'PRIORITY'
    valuetype = value.Integer() #???# Don't know if separate type is necessary

class Resources(Property):
    """ RFC 5545: Resources
    """
    name = 'RESOURCES'
    valuetype = value.Text()

class Status(Property):
    """ RFC 5545: Status
    """
    name = 'STATUS'
    valuetype = value.Text()
    #TODO# Check http://tools.ietf.org/search/rfc5545#section-3.8.1.11 for
    #TODO@ further properties to be included

class Summary(Property):
    """ RFC 5545: Summary
    """
    name = 'SUMMARY'
    valuetype = value.Text()

# RFC 5545: Date and Time Component Properties
# http://tools.ietf.org/search/rfc5545#section-3.8.2
class Completed(Property):
    """ RFC 5545: Date-Time Completed
    """
    name = 'COMPLETED'
    valuetype = value.DateTime()

class Dtend(Property):
    """ RFC 5545: Date-Time End
    """
    name = 'DTEND'
    valuetype = value.DateTime() #TODO# The default value type is DATE-TIME. 
                                 #TODO# The value type can be set to a DATE 
                                 #TODO# value type.
    
class Due(Property):
    """ RFC 5545: Date-Time Due
    """
    name = 'DUE'
    valuetype = value.DateTime() #TODO# The default value type is DATE-TIME. 
                                 #TODO# The value type can be set to a DATE 
                                 #TODO# value type.

class Dtstart(Property):
    """ RFC 5545: Date-Time Start
    """
    name = 'DTSTART'
    valuetype = value.DateTime() #TODO# The default value type is DATE-TIME. 
                                 #TODO# The value type can be set to a DATE 
                                 #TODO# value type.

class Duration(Property):
    """ RFC 5545: Duration
    """
    name = 'DURATION'
    valuetype = value.Duration()

class Freebusy(Property):
    """ RFC 5545: Free/Busy Time
    """
    name = 'FREEBUSY'
    valuetype = value.Period()

class Transp(Property):
    """ RFC 5545: Time Transparency
    """
    name = 'TRANSP'
    valuetype = value.Text()

# RFC 5545: Time Zone Component Properties
# http://tools.ietf.org/search/rfc5545#section-3.8.3
class Tzid(Property):
    """ RFC 5545: Time Zone Identifier
    """
    name = 'TZID'
    valuetype = value.Text()

class Tzname(Property):
    """ RFC 5545: Time Zone Name
    """
    name = 'TZNAME'
    valuetype = value.Text()

class Tzoffsetfrom(Property):
    """ RFC 5545: Time Zone Offset From
    """
    name = 'TZOFFSETFROM'
    valuetype = value.UtcOffset()

class Tzoffsetto(Property):
    """ RFC 5545: Time Zone Offset To
    """
    name = 'TZOFFSETTO'
    valuetype = value.UtcOffset()

class Tzurl(Property):
    """ RFC 5545: Time Zone URL
    """
    name = 'TZURL'
    valuetype = value.Uri()

# RFC 5545: Relationship Component Properties
# http://tools.ietf.org/search/rfc5545#section-3.8.4
class Attendee(Property):
    """ RFC 5545: Attendee
    """
    name = 'ATTENDEE'
    valuetype = value.CalAddress()

class Contact(Property):
    """ RFC 5545: Contact
    """
    name = 'CONTACT'
    valuetype = value.Text()

class Organizer(Property):
    """ RFC 5545: Organizer
    """
    name = 'ORGANIZER'
    valuetype = value.CalAddress()

class RecurrenceId(Property):
    """ RFC 5545: Recurrence ID
    """
    name = 'RECURRENCE-ID'
    #TODO# The default value type is DATE-TIME.  The value type can
    #TODO# be set to a DATE value type.  This property MUST have the same
    #TODO# value type as the "DTSTART" property contained within the
    #TODO# recurring component.  Furthermore, this property MUST be specified
    #TODO# as a date with local time if and only if the "DTSTART" property
    #TODO# contained within the recurring component is specified as a date
    #TODO# with local time.
    valuetype = value.DateTime()

class RelatedTo(Property):
    """ RFC 5545: Related To
    """
    name = 'RELATED-TO'
    valuetype = value.Text()

class Url(Property):
    """ RFC 5545: Uniform Resource Locator
    """
    name = 'URL'
    valuetype = value.Uri()

class Uid(Property):
    """ RFC 5545: Unique Identifier
    """
    name = 'UID'
    valuetype = value.Text()

# RFC 5545: Recurrence Component Properties
# http://tools.ietf.org/search/rfc5545#section-3.8.5
class Exdate(Property):
    """ RFC 5545: Exception Date-Times
    """
    name = 'EXDATE'
    #TODO# This property defines the list of DATE-TIME exceptions for
    #TODO# recurring events, to-dos, journal entries, or time zone
    #TODO# definitions.
    valuetype = value.DateTime()

# RFC 5545: Deprecated
#OLD# class Exrule(Property):
#OLD#     """ RFC 5545: 
#OLD#     """

class Rdate(Property):
    """ RFC 5545: Recurrence Date-Times
    """
    name = 'RDATE'
    #TODO# The default value type for this property is DATE-TIME.
    #TODO# The value type can be set to DATE or PERIOD.
    valuetype = value.DateTime()

#???# New since 5545?
#TODO# Look into spec. It's veeery extensive, might need to add
#TODO# some properties
class Rrule(Property):
    """ RFC 5545: Recurrence Rule
    """
    name = 'RRULE'
    valuetype = value.Recur()

# RFC 5545: Alarm Component Properties
# http://tools.ietf.org/search/rfc5545#section-3.8.6
class Action(Property):
    """ RFC 5545: Action
    """
    name = 'ACTION'
    valuetype = value.Text()

class Repeat(Property):
    """ RFC 5545: Repeat Count
    """
    name = 'REPEAT'
    valuetype = value.Integer() #???# Don't know if separate type is necessary

class Trigger(Property):
    """ RFC 5545: Trigger
    """
    name = 'TRIGGER'
    #TODO# The default value type is DURATION.  The value type can
    #TODO# be set to a DATE-TIME value type, in which case the value MUST
    #TODO# specify a UTC-formatted DATE-TIME value.
    valuetype = value.Duration()

# RFC 5545: Change Management Component Properties
# http://tools.ietf.org/search/rfc5545#section-3.8.7
class Created(Property):
    """ RFC 5545: Date-Time Created
    """
    name = 'CREATED'
    valuetype = value.DateTime()

class Dtstamp(Property):
    """ RFC 5545: Date-Time Stamp
    """
    name = 'DTSTAMP'
    valuetype = value.DateTime()

class LastModified(Property):
    """ RFC 5545: Last Modified
    """
    name = 'LAST-MODIFIED'
    valuetype = value.DateTime()

class Sequence(Property):
    """ RFC 5545: Sequence Number
    """
    name = 'SEQUENCE'
    valuetype = value.Integer()

# RFC 5545: Miscellaneous Component Properties
# http://tools.ietf.org/search/rfc5545#section-3.8.8
class RequestStatus(Property):
    """ RFC 5545: Request Status
    """
    name = 'REQUEST-STATUS'
    valuetype = value.Text()

