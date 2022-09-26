#!/usr/bin/python3
def uppercase(str):
    temp_string = ""
    for character in str:
        if ord(character) > 96 and ord(character) < 123:
            temp_string = temp_string + chr(ord(character) - 32)
        else:
            temp_string = temp_string + character
    print("{}".format(temp_string))
