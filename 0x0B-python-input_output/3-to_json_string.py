#!/usr/bin/python3

import json
"""creates a function that returns a json representation of an object"""


def to_json_string(my_obj):
    """returns a json representation of an objec(string)"""
    return json.dumps(my_obj)
