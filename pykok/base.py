#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Base Class has common attributes for all classes
"""

from pykok.settings import __dbug__


class Base(object):
    """
    Common attributes
    """
    def __init__(self, **kwargs):
        super(Base, self).__init__()
        self._primary_key = None
        self._name = None
        self._description = None
        self._tags = []
        for prop, val in kwargs.items():
            setattr(self, prop, val)

    def __repr__(self):
        printer = 'Base (primary_key:{primary_key}, name:{name}, \
                            description:{description}, tags:{tags})'
        return printer.format(primary_key=self.primary_key, name=self.name, \
                                description=self.description, tags=self.tags)

    @property
    def primary_key(self):
        """
        Unique ID for each class
        """
        return self._primary_key
    @primary_key.setter
    def primary_key(self, primary_key):
        self._primary_key = primary_key

    @property
    def name(self):
        """
        Just a Name for human
        """
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        """
        Long description, to add usefull info
        """
        return self._description
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def tags(self):
        """
        a few words
        """
        return self._tags
    @tags.setter
    def tags(self, tags):
        self._tags = tags
