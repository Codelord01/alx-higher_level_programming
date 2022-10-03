#!/usr/bin/python3
"""creates a better rectangle from 0-rectangle"""


class Rectangle:
    """Class that create a better rectangle"""

    def __init__(self, width=0, height=0):
        """The init method for instance variables"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """The getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the width"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
