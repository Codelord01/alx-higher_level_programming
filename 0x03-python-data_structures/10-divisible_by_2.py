#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for number in my_list:
        if number % 2 == 0:
            new_list.insert(my_list.index(number), True)
        else:
            new_list.insert(my_list.index(number), False)
    return new_list
