#!/usr/bin/env python3
def remove_char_at(str, n):
    new_str = ""
    str_len = len(str)
    i = 0
    while str_len > 0:
        if i != n:
            new_str += str[i]
        i = i + 1
        str_len = str_len - 1
    return new_str
