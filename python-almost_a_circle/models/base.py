#!/usr/bin/python3
"""module for Base class"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to_json_string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
