#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    string_len = len(roman_string)
    loop_index = 0
    roman_sum = roman_d[roman_string[loop_index]]
    if isinstance(roman_string, str):
        if string_len == 1:
            return roman_d[roman_string[loop_index]]
        while string_len - loop_index != 1:
            before = roman_d[roman_string[loop_index]]
            ahead = roman_d[roman_string[loop_index + 1]]
            if before < ahead:
                roman_sum += - roman_d[roman_string[loop_index + 1]]
            else:
                roman_sum += roman_d[roman_string[loop_index + 1]]
            loop_index += 1
        if roman_sum < 0:
            return -roman_sum
        else:
            return roman_sum
    return 0
