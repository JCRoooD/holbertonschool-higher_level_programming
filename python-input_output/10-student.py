#!/usr/bin/python3


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initializes the instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            new_dict = {}
            for x in attrs:
                if str(x) in self.__dict__:
                    new_dict[x] = self.__dict__[x]
            return new_dict
        return self.__dict__
