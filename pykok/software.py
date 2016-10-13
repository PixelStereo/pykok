#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
A software is a virtual item.
It has specific
In case you have 20 chairs, it is a group of twenty different items
"""

from pykok.settings import __dbug__
from pykok.item import Item

class Software(Item):
    """
    It is a stuff we want to know where it is, when and its specifications
    Photos is a good point too.
    dimensions (exports possible en pieds ou en metrique)
    """
    def __init__(self, **kwargs):
        super(Software, self).__init__()
        self._serial = None
        self._version = None
        for prop, val in kwargs.items():
            setattr(self, prop, val)

    def __repr__(self):
        printer = 'Software (primary_key:{primary_key}, name:{name}, version:{version})'
        return printer.format(primary_key=self.primary_key, name=self.name, version=self.version)

    @property
    def version(self):
        """
        Version of a software
        TODO : How to do when we already have a software and we buy an upgrade?
        """
        return self._version
    @version.setter
    def version(self, version):
        self._version = version
