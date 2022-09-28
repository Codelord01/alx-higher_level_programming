#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(list(a_dictionary))
    i = 0
    for value in range(len(list(a_dictionary))):
        print("{}: {}".format(sorted_list[i], a_dictionary[sorted_list[i]]))
        i += 1
