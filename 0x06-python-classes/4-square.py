#!/usr/bin/python3
"""A class Square that defines a square
by: (based on 1-square.py)

"""


class Square:
    """Square class with a private attribute
    size.

    """

    def __init__(self, size=0):
        """Initializes the size variable as a private
        instance artribute
        Args:
        __size (int): The __size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """
        returns the value of self as a getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter that sets the values
        """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Finds the areas of the square
        """
        return self.__size ** 2
