#!/usr/bin/python3
""""student module"""


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
                if str(x) == "first_name":
                    new_dict[x] = self.first_name
                elif x == "last_name":
                    new_dict[x] = self.last_name
                elif x == "age":
                    new_dict[x] = self.age
            return new_dict
        else:
            return self.__dict__
        
    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            if key == "first_name":
                self.first_name = value
            elif key == "last_name":
                self.last_name = value
            elif key == "age":
                self.age = value
