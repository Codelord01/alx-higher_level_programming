#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord(character) > 96 and ord(character) < 123:
            print("{:c}".format(ord(character)-32), end="")
        else:
            print("{}".format(character), end="")
