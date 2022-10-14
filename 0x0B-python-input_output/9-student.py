#!/usr/bin/python3
"""creates a class student"""


class Student:
    """a student class"""

    def ___init___(self, first_name, last_name, age):
        """the init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        res = self.__dict__.copy()
        return res
