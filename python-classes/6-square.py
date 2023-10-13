#!/usr/bin/python3
"""Module contains square class"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set position"""
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return area of Square"""
        return self.__size ** 2

    def my_print(self):
        """"Print Square using #"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
