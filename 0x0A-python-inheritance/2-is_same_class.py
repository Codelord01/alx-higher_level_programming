#!/usr/bin/python3
""""creates a function that checks for object type"""


def is_same_class(obj, a_class):
    """returns true if an object is exactly an instance of a specified class"""
    return True if type(obj) == a_class else False
