#!/usr/bin/python3

"""creates a function that returns a json representation of an object"""
import json


def to_json_string(my_obj):
    """returns a json representation of an objec(string)"""
    return json.dumps(my_obj)
