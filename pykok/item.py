#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Item is one thing that we want to inventoriate
In case you have 20 chairs, it is a group of twenty different items
"""

from pykok.settings import __dbug__
from pykok.base import Base

class Item(Base):
    """
    It is a stuff we want to know where it is, when and its specifications
    Photos is a good point too.
    dimensions (exports possible en pieds ou en metrique)
    """
    index = 0
    def __init__(self, **kwargs):
        super(Item, self).__init__()
        Item.index += 1
        self._primary_key = Item.index
        self._serial = None
        self._model = None
        self._brand = None
        self._price = None
        self._location = None
        for prop, val in kwargs.items():
            setattr(self, prop, val)

    def __repr__(self):
        printer = 'Item (primary_key:{primary_key}, name:{name}, location:{location})'
        return printer.format(primary_key=self.primary_key, name=self.name, location=self.location)

    @property
    def serial(self):
        """
        Serial Number
        """
        return self._serial
    @serial.setter
    def serial(self, serial):
        self._serial = serial


    @property
    def model(self):
        """
        Model
        """
        return self._model
    @model.setter
    def model(self, model):
        self._model = model

    @property
    def brand(self):
        """
        Brand
        """
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def price(self):
        """
        price of purchase
        """
        return self._price
    @price.setter
    def price(self, price):
        self._price = price

    @property
    def location(self):
        """
        Location where the item is now
        """
        return self._location
    @location.setter
    def location(self, location):
        self._location = location
