#!/usr/bin/python3
""""Module for Rectangle class."""


class Rectangle:
    """Defines a rectangle"""
    
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height
            Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__width + self.__height)

    def __str__(self):
        """Return string representation of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            rect += "\n"
        return rect[:-1]

    def __repr__(self):
        """Return string representation of Rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
