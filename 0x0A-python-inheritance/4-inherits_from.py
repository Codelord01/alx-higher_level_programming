#!/usr/bin/python3
"""creates a function"""


def inherits_from(obj, a_class):
    """checks for base or derived class"""
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        False
