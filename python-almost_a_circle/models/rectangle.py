#!/usr/bin/python3
"""module for rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """returns rectangle with #"""
        for z in range(self.__y):
            print()
        for z in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self) -> str:
        """returns string representation of rectangle"""
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Update the rectangle"""
        if args:
            if i >= 1:
                self.id = args[0]
            elif i >= 2:
                self.width = args[1]
            elif i >= 3:
                self.height = args[2]
            elif i >= 4:
                self.x = args[3]
            elif i >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}  # dictionary representation
