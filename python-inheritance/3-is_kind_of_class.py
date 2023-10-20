#!/usr/bin/python3
"""is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """calling kind of class function"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
