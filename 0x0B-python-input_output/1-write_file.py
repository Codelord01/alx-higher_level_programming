#!/usr/bin/python3
"""creates a function that writes a file in utf-8 encoding"""


def write_file(filename="", text=""):
    """writes into a file in utf-8 encoding"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
