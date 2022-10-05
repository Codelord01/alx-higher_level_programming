#!/usr/bin/python3

"""Creates a function
    The function takes two arguments
    a and b and adds them up
    And returns a result which is an int
"""


def add_integer(a, b=98):
    """ argument 1 =a
        argument 2 = b
    """

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
