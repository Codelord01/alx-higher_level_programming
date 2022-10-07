#!/usr/bin/python3
"""Creates an empty class"""


class BaseGeometry:
    """Geometry class with only method for area"""
    def area(self):
        raise Exception("area() is not implemented")
