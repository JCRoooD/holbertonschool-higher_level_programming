#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """returns True if object is an instance of a class that inherited"""
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
