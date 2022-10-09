#!/usr/bin/python3
"""creates a function which creates an object from a json file"""
import json


def load_from_json_file(filename):
    """creates a json object from a json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
