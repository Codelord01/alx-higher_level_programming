#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num_len = len(str(number)) - 1
        number *= -1
    else:
        num_len = len(str(number))
    while num_len != 0:
        number = number % 10
        num_len = num_len - 1
    print(number, end="")
    return number
