#!/usr/bin/python3
"""Creates an empty class"""


class BaseGeometry:
    """Geometry class with only method for area"""
    def area(self):
        """finds the area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the values to get int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
