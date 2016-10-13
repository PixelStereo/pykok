#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys

sys.path.append(os.path.abspath('./../'))

import time
import datetime
from pykok.settings import __dbug__
from pykok.api import new_item, new_location


loc_1 = new_location(name='maison')
loc_2 = new_location(name='studio', address='Rebeval')
loc_3 = new_location()
item_1 = new_item(category='software', name='Ableton Live', version='9.7')
item_2 = new_item(category='hardware', name='Mac Pro Hermès', weight=22.2, price=2800)
move_1 = item_1.location = loc_1


class TestAll(unittest.TestCase):

    def test_create_location(self):
        
        self.assertEqual(loc_1.name, 'maison')
        print('LOC_1', loc_1)
        self.assertEqual(loc_2.address, 'Rebeval')
        print('LOC_2', loc_2)
        print('LOC_3', loc_3)

    def test_create_item(self):
        self.assertEqual(item_1.category, 'software')
        self.assertEqual(item_1.name, 'Ableton Live')
        self.assertEqual(item_1.version, '9.7')
        print('ITEM_1', item_1)
        self.assertEqual(item_2.category, 'hardware')
        self.assertEqual(item_2.name, 'Mac Pro Hermès')
        self.assertEqual(item_2.weight, 22.2)
        self.assertEqual(item_2.price, 2800)
        self.assertEqual(item_2.dimensions, None)
        print('ITEM_2', item_2)

    def test_create_movement(self):
        self.assertEqual(item_1.location, loc_1)

if __name__ == '__main__':
    unittest.main()
