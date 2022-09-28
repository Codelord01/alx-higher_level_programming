#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        key_list = list(a_dictionary)
        max_key = key_list[0]
        max_score = a_dictionary[key_list[0]]
        for key in key_list:
            if a_dictionary[key] > max_score:
                max_key = key
                max_score = a_dictionary[key]
        return max_key
