#!/usr/bin/python3
"""creates function that writes an object to a
text file using a json representation"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file using json format"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
