#!/usr/bin/python
#
# Author: Lutz Engels <lutz.engels@os3.nl>

# superclass
class Parameter():
    def __init__(self, *args, **kwargs):
        #TODO#
        pass

# subclasses
class Altrep(Parameter):
    """RFC 5545: Alternate text representation
    """
    #TODO#
    pass

class Cn(Parameter):
    """ RFC 5545: Common name 
    """
    #TODO#
    pass

class Cutype(Parameter):
    """ RFC 5545: Calendar user type
    """
    #TODO#
    pass

class Delfrom(Parameter):
    """ RFC 5545: Delegator
    """
    #TODO#
    pass

class Delto(Parameter):
    """ RFC 5545: Delegatee
    """
    #TODO#
    pass

class Dir(Parameter):
    """ RFC 5545: Directory entry
    """
    #TODO#
    pass

class Encoding(Parameter):
    """ RFC 5545: Inline encoding
    """
    #TODO#
    pass

class Fmttype(Parameter):
    """ RFC 5545: Format type
    """
    #TODO#
    pass

class Fbtype(Parameter):
    """ RFC 5545: Free/busy time type
    """
    #TODO#
    pass

class Language(Parameter):
    """ RFC 5545: Language for text
    """
    #TODO#
    pass

class Member(Parameter):
    """ RFC 5545: Group or list membership
    """
    #TODO#
    pass

class Partstat(Parameter):
    """ RFC 5545: Participation status
    """
    #TODO#
    pass

class Range(Parameter):
    """ RFC 5545: Recurrence identifier range
    """
    #TODO#
    pass

class Trigrel(Parameter):
    """ RFC 5545: Alarm trigger relationship
    """
    #TODO#
    pass

class Reltype(Parameter):
    """ RFC 5545: Relationship type
    """
    #TODO#
    pass

class Role(Parameter):
    """ RFC 5545: Participation role
    """
    #TODO#
    pass

class Rsvp(Parameter):
    """ RFC 5545: RSVP expectation
    """
    #TODO#
    pass

class Sentby(Parameter):
    """ RFC 5545: Sent by
    """
    #TODO#
    pass

class Tzid(Parameter):
    """ RFC 5545: Reference to time zone object
    """
    #TODO#
    pass

class Valuetype(Parameter):
    """ RFC 5545: Property value data type
    """
    #TODO#
    pass


class Other(Parameter):
    """ RFC 5545:
    other-param   = (iana-param / x-param)

    iana-param  = iana-token "=" param-value *("," param-value)
    ; Some other IANA-registered iCalendar parameter.

    x-param     = x-name "=" param-value *("," param-value)
    ; A non-standard, experimental parameter.
    """
    #TODO#
    pass

