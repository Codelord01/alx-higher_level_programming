#!/usr/bin/python3
"""prints out a square"""


def print_square(size):
    """
    Prints out the square by taking its size a parameter
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for number in range(0, size):
        for number in range(0, size):
            print("#", end = "")
        print("")
