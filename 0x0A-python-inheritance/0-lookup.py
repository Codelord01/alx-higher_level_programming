#!/usr/bin/python3
"""creates a function that prints all object attributes"""


def lookup(obj):
    """function that prints out all object attritutes"""
    attributes = dir(obj)
    return attributes
