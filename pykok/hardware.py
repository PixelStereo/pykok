#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Item is one thing that we want to inventoriate
In case you have 20 chairs, it is a group of twenty different items
"""

from pykok.settings import __dbug__
from pykok.item import Item

class Hardware(Item):
    """
    It is a stuff we want to know where it is, when and its specifications
    Photos is a good point too.
    dimensions (exports possible en pieds ou en metrique)
    """
    def __init__(self, **kwargs):
        super(Hardware, self).__init__()
        self._dimensions = None
        self._weight = None
        for prop, val in kwargs.items():
            setattr(self, prop, val)

    def __repr__(self):
        printer = 'Hardware (primary_key:{primary_key}, name:{name}, dimensions:{dimensions}, weight:{weight})'
        return printer.format(primary_key=self.primary_key, name=self.name, dimensions=self.dimensions, weight=self.weight)

    @property
    def dimensions(self):
        return self._dimensions
    @dimensions.setter
    def dimensions(self, dimensions):
        self._dimensions = dimensions

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, weight):
        self._weight = weight
