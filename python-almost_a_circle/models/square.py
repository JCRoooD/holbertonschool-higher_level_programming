#!/usr/bin/python3
""""module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)  # string rep of square

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes"""
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
        """dictionary representation"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
