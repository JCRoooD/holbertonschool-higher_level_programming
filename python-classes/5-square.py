#!/usr/bin/python3
""""Module for Square class"""


class Square:
    """"class Square with private attribute instance"""
    def __init__(self, size=0):
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

    def my_print(self):
        """Print Square using #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
