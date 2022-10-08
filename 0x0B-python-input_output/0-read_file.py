#!/usr/bin/python3
"""creates a function that reads a text file in UTF-8"""


def read_file(filename=""):
    """function that reads a rile in UTF-8"""
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data)
