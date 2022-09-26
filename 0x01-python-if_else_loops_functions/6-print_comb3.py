#!/usr/bin/python3
for number in range(0, 9, 1):
    for sub in range(number+1, 10, 1):
        if number == 8 and sub == 9:
            print("{}{}".format(number, sub))
        else:
            print("{}{}, ".format(number, sub), end="")
