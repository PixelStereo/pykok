#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Location is an Area that might stock items or group of items.
A Location have an address, that might change
A Location must have a Personn as contact
"""

from pykok.software import Software
from pykok.hardware import Hardware
from pykok.location import Location

_items = []

def new_item(**kwargs):
    """
	Create a new item
	need a 'category' argument with a value (software, hardware)
	"""
    if not 'category'in kwargs.keys():
        print('need a category to create an item')
        return False
    else:
        if kwargs['category'] == 'software':
            new_soft = Software(**kwargs)
            _items.append(new_soft)
            return new_soft
        elif kwargs['category'] == 'hardware':
            new_hard = Hardware(**kwargs)
            _items.append(new_hard)
            return new_hard

def new_location(**kwargs):
    """
	create a new location
	"""
    return Location(**kwargs)

def get_items(**kwargs):
    """
    get a list of items
    """
    if 'name' in kwargs.keys():
        return [item for item in _items if kwargs['name'] in item.name]
    elif 'purchase_date' in kwargs.keys():
        return [item for item in _items if kwargs['purchase_date'] == item.purchase_date]
    else:
        return _items
