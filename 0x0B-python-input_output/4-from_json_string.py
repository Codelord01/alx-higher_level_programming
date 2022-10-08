#!/usr/bin/python3
"""creates a function that converts a python data structure to json"""

import json


def from_json_string(my_str):
    """return a json representation of a python data structure"""
    return json.loads(my_str)
