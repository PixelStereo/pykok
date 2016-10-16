#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Import items throught a CSV file

"""
import time
from pykok.settings import __dbug__
from pykok.api import new_item, new_location, get_items

import csv
from pprint import pprint

# read the csv file
reader = csv.DictReader(open('test-csv.csv', 'rb'))
# make a list of all the items (all the lines)
dict_list = []
for line in reader:
    dict_list.append(line)
# enumarate each item
for item in dict_list:
	new_item(category=item['category'], name=item['name'], serial=item['serial'], \
				description=item['description'], notes=item['notes'], purchase_date=item['purchase_date'], \
				purchase_price=item['purchase_price'], warranty=item['warranty'])

print('--------------------------------------')
if __dbug__:
	pprint(str(len(get_items())) + ' items have been created' )
print('--------------------------------------')
pprint(get_items())
print('--------------------------------------')
pprint(get_items(name='Mac'))
print('--------------------------------------')
quit()

from flask import Flask
app = Flask(__name__)

@app.route("/items")
def hello():
        return [item.name for item in get_items()]

if __name__ == "__main__":
    app.run()