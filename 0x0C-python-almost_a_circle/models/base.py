#!/usr/bin/python3

"""
creates the base class
"""


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """
        instance init method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
