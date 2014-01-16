#!/usr/bin/python
#
# Author: Lutz Engels <lutz.engels@os3.nl>

import property

def list_subclasses_and_their_attributes(superclass):
    """Nomen est omen.
    """
    for subs in superclass.__subclasses__():
        print subs.__name__, subs.name,
        print dir(subs)
        print
# And here we go
list_subclasses_and_their_attributes(property.Property)
