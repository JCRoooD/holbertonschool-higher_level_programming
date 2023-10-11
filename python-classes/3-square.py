#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class with private attribute"""
    
    def __init__(self, size=0):
        """Initialize Square with size attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be > 0")
        else:
            self._Square__size = size
        
    def area(self):
        """Return area of Square"""
        return self._Square__size ** 2
