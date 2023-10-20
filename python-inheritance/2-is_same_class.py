#!/usr/bin/python3
"""is_same_class function"""


def is_same_class(obj, a_class):
    """returns True if object is exactly an instance of specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
