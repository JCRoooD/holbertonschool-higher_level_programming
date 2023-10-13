#!/usr/bin/python3
"""Defines a square printing function"""


def print_square(size):
    """Print a square with the # character"""
    if type(size) is not int and size is not float < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
