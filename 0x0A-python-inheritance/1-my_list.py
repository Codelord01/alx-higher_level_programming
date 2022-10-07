#!/usr/bin/python3
"""
creates a class that inherit from the class list
"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """sorts the list in asscending order"""

        print(sorted(self))
