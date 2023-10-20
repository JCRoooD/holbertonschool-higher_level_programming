#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """empty class"""
    pass

    def area(self):
        if self:
            raise Exception("area() is not implemented")
