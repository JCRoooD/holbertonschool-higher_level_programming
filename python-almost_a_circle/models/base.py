#!/usr/bin/python3
"""module for Base class"""


class Base:
    """Base Class"""
    __nb__objects = 0

    def __init__(self, id=None):
        """init method for Base class"""
        if id is None:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
        else:
            self.id = id
