#!/usr/bin/python3
"""defines a square that inherits from Rectangle"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class that describes a square"""
    def __init__(self, size):
        Rectangle.integer_validator(self, 'size', size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
