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
            return Software(**kwargs)
        elif kwargs['category'] is 'hardware':
            return Hardware(**kwargs)

def new_location(**kwargs):
    """
	create a new location
	"""
    return Location(**kwargs)