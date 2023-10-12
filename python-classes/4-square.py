#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class with private attribute instance"""
    
    def __innit__(self, size=0):
        """Initialize Square with size attribute"""
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter method to set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value
    
    def area(self):
        """Return area of Square"""
        return self.__size ** 2
