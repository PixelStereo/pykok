#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Movement is base class for all movements
It is an abstract Class that cannot be instanciate
"""

from pykok.settings import __dbug__
from pykok.base import Base
from datetime import datetime

class Movement(Base):
    """
    It is a movement of an attribute from a value to another value
    """
    index = 0
    def __init__(self, **kwargs):
        super(Movement, self).__init__()
        Movement.index += 1
        self._primary_key = Movement.index
        self._timestamp = None
        for prop, val in kwargs.items():
            setattr(self, prop, val)

    def __repr__(self):
        printer = 'Movement (primary_key:{primary_key}, name:{name}, timestamp:{timestamp})'
        return printer.format(primary_key=self.primary_key, name=self.name, timestamp=self.timestamp)

    @property
    def timestamp(self):
        """
        this is a the exact date when the movement happened
        """
        return self._timestamp
    @timestamp.setter
    def timestamp(self, timestamp):
        if timestamp == None:
            self._timestamp = datetime.now()
        else:
            self._timestamp = timestamp
        