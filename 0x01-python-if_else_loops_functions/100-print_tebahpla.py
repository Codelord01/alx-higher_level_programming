#!/usr/bin/python3
for character in range(90, 64, -1):
    if character % 2 == 1:
        print("{:c}".format(character), end="")
    else:
        print("{:c}".format(character + 32), end="")
