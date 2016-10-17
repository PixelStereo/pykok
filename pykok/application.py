#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Application is the main base app
"""

from pykok.settings import __dbug__
from pykok.base import Base
from pykok.software import Software
from pykok.hardware import Hardware
from pykok.location import Location

class Application(Base):
    """
    It is the base application
    """
    def __init__(self, **kwargs):
        super(Application, self).__init__()
        self._items = []
        self._locations = []
        for prop, val in kwargs.items():
            setattr(self, prop, val)

    def __repr__(self):
        printer = 'Application (items:{items}, locations:{locations})'
        return printer.format(items=len(self.items), locations=len(self.locations))

    @property
    def items(self):
        """
        List of the items of this app
        """
        return self._items

    @property
    def locations(self):
        """
        List of locations of this app
        """
        return self._locations

    def import_csv(self, filepath):
        """
        import items from a csv file
        The file must have the followings columns : 
        category, name, serial, description, notes, purchase_date, purchase_price, warranty
        """
        try:
            import csv
            # read the csv file
            if __dbug__:
                print('try to import file ' + filepath)
            reader = csv.DictReader(open(filepath, 'rb'))
            # make a list of all the items (all the lines)
            dict_list = []
            for line in reader:
                dict_list.append(line)
            # enumarate each item
            for item in dict_list:
                self.new_item(category=item['category'], name=item['name'], serial=item['serial'], \
                            description=item['description'], notes=item['notes'], purchase_date=item['purchase_date'], \
                            purchase_price=item['purchase_price'], warranty=item['warranty'])
            if __dbug__:
                print(str(len(self.get_items())) + ' items have been created' )
            return True
        except IOError:
            if __dbug__:
                print('Error - can not import file ' + filepath)
            return False


    def new_item(self, **kwargs):
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
                self._items.append(new_soft)
                return new_soft
            elif kwargs['category'] == 'hardware':
                new_hard = Hardware(**kwargs)
                self._items.append(new_hard)
                return new_hard

    def new_location(self, **kwargs):
        """
        create a new location
        """
        return Location(**kwargs)

    def get_items(self, **kwargs):
        """
        get a list of items
        """
        if 'name' in kwargs.keys():
            return [item for item in self._items if kwargs['name'] in item.name]
        elif 'purchase_date' in kwargs.keys():
            return [item for item in self._items if kwargs['purchase_date'] == item.purchase_date]
        else:
            return self._items
