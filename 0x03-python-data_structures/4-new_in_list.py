#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    new_list = [x for x in my_list]
    if idx < 0:
        return my_list
    elif idx > list_len:
        return my_list
    else:
        for number in my_list:
            if my_list.index(number) == idx:
                new_list[idx] = element
    return new_list
