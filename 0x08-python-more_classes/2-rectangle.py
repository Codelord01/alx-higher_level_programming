#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """Defines the implementation of a rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property retriever, for retreiving"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter, for setting"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property retriever, for retreiving
        the rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Finds the area of the rectangle"""
        rectangle_perimeter = self.__width * self.__height
        return rectangle_perimeter

    def perimeter(self):
        """Finds the perimeter of the area"""

        if self.__width == 0 or self.__height == 0:
            return 0

        rectangle_area = (2 * self.__width) + (2 * self.__height)
        return rectangle_area