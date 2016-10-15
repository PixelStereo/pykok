#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Relocation is a Movement of an Item from a Location to another
It is a Class that inherit from Movement
"""

from pykok.settings import __dbug__
from pykok.movement import Movement
from datetime import datetime

class Relocation(Movement):
    """
    It is a movement of an attribute from a value to another value
    """
    index = 0
    def __init__(self, **kwargs):
        super(Relocation, self).__init__()
        Relocation.index += 1
        self._primary_key = Relocation.index
        for prop, val in kwargs.items():
            setattr(self, prop, val)

    def __repr__(self):
        printer = 'Relocation (primary_key:{primary_key}, name:{name}, timestamp:{timestamp}, new:{new})'
        return printer.format(primary_key=self.primary_key, name=self.name, timestamp=self.timestamp, new=self.new)
