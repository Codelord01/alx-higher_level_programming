#!/usr/bin/python3
"""creates a function that writes a file in utf-8 encoding"""


def append_write(filename="", text=""):
    """writes into a file in utf-8 encoding"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
