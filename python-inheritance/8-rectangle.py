#!/usr/bin/python3
"""Rectangle class inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry call"""
    def __init__(self, width, height):
        """init method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
