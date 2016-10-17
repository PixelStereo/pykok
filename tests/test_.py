#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys

sys.path.append(os.path.abspath('./../'))

import time
from pykok.settings import __dbug__
from pykok.api import app


loc_1 = app.new_location(name='maison')
loc_2 = app.new_location(name='studio', address='Rebeval')
loc_3 = app.new_location()
item_1 = app.new_item(category='software', name='Ableton Live', version='9.7')
item_2 = app.new_item(category='hardware', name='Mac Pro Hermès', weight=22.2, price=2800)
item_1.relocation(loc_1)
item_1.relocation(loc_2)


class TestAll(unittest.TestCase):
    print('------- FIRST TEST --------')
    def test_location(self):
        self.assertEqual(loc_1.name, 'maison')
        self.assertEqual(loc_2.address, 'Rebeval')

    def test_item(self):
        self.assertEqual(item_1.category, 'software')
        self.assertEqual(item_1.name, 'Ableton Live')
        self.assertEqual(item_1.version, '9.7')
        self.assertEqual(item_2.category, 'hardware')
        self.assertEqual(item_2.name, 'Mac Pro Hermès')
        self.assertEqual(item_2.weight, 22.2)
        self.assertEqual(item_2.price, 2800)
        self.assertEqual(item_2.dimensions, None)

    def test_movement(self):
        self.assertEqual(item_1.location, loc_2)

    def test_print(self):
        print('--- LOC_1 ---')
        print(loc_1)
        print('--- LOC_2 ---')
        print(loc_2)
        print('--- LOC_3 ---')
        print(loc_3)
        print('--- ITEM_1 ---')
        print(item_1)
        print('--- ITEM_2 ---')
        print(item_2)
        print('--- ITEM 1 RELOCATIONS ---')
        for reloc in item_1.relocations:
            print(reloc)


class TestSecond(unittest.TestCase):
    def __init__(self, arg):
        super(TestSecond, self).__init__()
        print('------- SECOND TEST --------')
        

if __name__ == '__main__':
    unittest.main()
