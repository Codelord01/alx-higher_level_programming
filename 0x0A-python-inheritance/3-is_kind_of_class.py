#!/usr/bin/python3
"""defines a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class """


def is_kind_of_class(obj, a_class):
    """returns true or false by checking the class and object"""
    return isinstance(obj, a_class)
