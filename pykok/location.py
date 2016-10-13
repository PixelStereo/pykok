#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Location is an Area that might stock items or group of items.
A Location have an address, that might change
A Location must have a Personn as contact
"""

from pykok.settings import __dbug__
from pykok.base import Base

class Location(Base):
    """
    It is a warehouse to stock items
    """
    index = 0
    def __init__(self, **kwargs):
        super(Location, self).__init__()
        Location.index += 1
        self._primary_key= Location.index
        self._name = None
        self._description = None
        self._address = None
        self._tags = []
        self._contact = None
        for prop, val in kwargs.items():
            setattr(self, prop, val)

    def __repr__(self):
        printer = 'Location (primary_key:{primary_key}, name:{name}, address:{address})'
        return printer.format(primary_key=self.primary_key, name=self.name, address=self.address)

    @property
    def address(self):
        """
        Physical address of the location
        """
        return self._address
    @address.setter
    def address(self, address):
        self._address = address

    @property
    def contact(self):
        """
        Person to contact about this location
        """
        return self._contact
    @contact.setter
    def contact(self, contact):
        self._contact = contact
