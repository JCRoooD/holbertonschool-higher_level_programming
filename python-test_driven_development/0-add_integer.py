#!/usr/bin/python3
"""This module contains a function that adds two integers."""


def add_integer(a, b=98):
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    if type(a) and type(b) is float:
        a = int(a)
        b = int(b)
    if type(a) and type(b) is int:
        a = int(a)
        b = int(b)
    return a + b
