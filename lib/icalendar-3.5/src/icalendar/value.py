#!/usr/bin/python
#
# Author: Lutz Engels <lutz.engels@os3.nl>

# superclass
class Value():
    def __init__(self, *args, **kwargs):
        #TODO#
        pass

# subclasses
# reflects http://tools.ietf.org/search/rfc5545#section-8.3.4
class Text(Value):
    #TODO#
    pass

class Uri(Value):
    #TODO#
    pass

class Geo(Value):
    #TODO#
    pass

class Integer(Value):
    #TODO#
    pass

class DateTime(Value):
    #TODO#
    pass

class Duration(Value):
    #TODO#
    pass

class Period(Value):
    #TODO#
    pass

class UtcOffset(Value):
    #TODO#
    pass

class CalAddress(Value):
    #TODO#
    pass

class DateTimeList(Value):
    #TODO#
    pass

class Recur(Value):
    #TODO#
    pass

