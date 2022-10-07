#!/usr/bin/python3
"creates rectangle that inherits from base geometry"


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class that defines rectangle"""

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
