#!/usr/bin/python3

from models.base import Base
"""
creates a class rectangle
"""


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init function for instance variables
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        self.__height = value

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @x.setter
    def y(self, value):
        """
        setter for y
        """
        self.__y = value
