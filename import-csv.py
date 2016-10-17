#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Import items throught a CSV file

"""

import time
from pykok.settings import __dbug__
from pykok.api import app

from pprint import pprint

app.import_csv('test-csv.csv')

print('--------------------------------------')
pprint(len(app.get_items()))
print('--------------------------------------')
pprint(app.get_items(name='Mac'))
print('--------------------------------------')
