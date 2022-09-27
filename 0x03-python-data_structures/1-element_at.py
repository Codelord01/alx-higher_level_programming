#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)
    if idx < 0:
        return None
    elif idx > list_len:
        return None
    else:
        for number in my_list:
            if my_list.index(number) == idx:
                return number
