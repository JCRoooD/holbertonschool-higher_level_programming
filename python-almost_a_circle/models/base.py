#!/usr/bin/python3
"""module for Base class"""

import json
import os.path as path


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

    def from_json_string(json_string):
        """method from_json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """method to save to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = []
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                f.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """method create"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """method load from file"""
        filename = cls.__name__ + ".json"
        if not path.exists(filename):
            return []
        with open(filename) as f:
            list_dicts = cls.from_json_string(f.read())
            list_objs = []
            for dict in list_dicts:
                list_objs.append(cls.create(**dict))
            return list_objs
