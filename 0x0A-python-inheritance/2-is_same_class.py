#!/usr/bin/python3
""""creates a function that checks for object type"""


def is_same_class(obj, a_class):
    """returns true if an object is exactly an instance of a specified class"""
    return isinstance(obj, a_class)
