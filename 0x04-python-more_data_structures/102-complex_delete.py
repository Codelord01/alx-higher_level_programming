#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    dict_keys = list(a_dictionary)
    for key in dict_keys:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
