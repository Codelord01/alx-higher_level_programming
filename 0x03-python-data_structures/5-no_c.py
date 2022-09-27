#!/usr/bin/python3
def no_c(my_string):
    new_string = [x for x in my_string]
    for character in my_string:
        if character == 'c' or character == 'C':
            new_string.remove(character)
    new_string = ''.join(new_string)
    return new_string
