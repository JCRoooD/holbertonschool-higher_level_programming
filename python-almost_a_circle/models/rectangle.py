#!/usr/bin/python3
"""module for rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

