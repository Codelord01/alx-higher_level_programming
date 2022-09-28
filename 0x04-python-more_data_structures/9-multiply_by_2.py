#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_list = list(a_dictionary)
    new_dict = {}
    for value in dict_list:
        new_dict[value] = a_dictionary[value] * 2
    return new_dict
