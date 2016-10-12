#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Item is one thing that we want to inventoriate
In case you have 20 chairs, it is a group of twenty different items
"""

from pykok.settings import __dbug__
from pykok.location import Location

class Item(Location):
    index = 0
    """
    It is a stuff we want to know where it is, when and its specifications
    Photos is a good point too.
    dimensions (exports possible en pieds ou en metrique)
    """
    def __init__(self, **kwargs):
        super(Item, self).__init__()
        Item.index += 1
        self._primary_key= Item.index
        self._name = None
        self._model = None
        self._contacts = None
        self._brand = None
        self._price = None
        self._preffered_contact = None
        for prop, val in kwargs.items():
            setattr(self, prop, val)

    def __repr__(self):
        printer = 'Location (primary_key:{primary_key}, name:{name}, tags:{tags})'
        return printer.format(primary_key=self.primary_key, name=self.name, tags=self.tags)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def tags(self):
        return self._tags
    @tags.setter
    def tags(self, tags):
        self._tags = tags

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, address):
        self._address = address

    @property
    def primary_key(self):
        return self._primary_key
    @primary_key.setter
    def primary_key(self, primary_key):
        self._primary_key = primary_key

    @property
    def contacts(self):
        return self._contacts
    @contacts.setter
    def contacts(self, contacts):
        self._contacts = contacts

    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = price

    @property
    def preffered_contact(self):
        return self._preffered_contact
    @preffered_contact.setter
    def preffered_contact(self, preffered_contact):
        self._preffered_contact = preffered_contact