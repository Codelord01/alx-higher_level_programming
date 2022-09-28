#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    for number in my_list:
        if my_list.index(number) == idx:
            my_list.remove(number)
    return my_list
