#!/usr/bin/python3
if __name__ == '__main__':

    import sys

    arg_len = len(sys.argv)
    arg_index = 1

    if arg_len == 1:
        print("0 arguments.")
    elif arg_len == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_len - 1))
    while arg_len - 1 > 0:
        print("{}: {}".format(arg_index, sys.argv[arg_index]))
        arg_len = arg_len - 1
        arg_index = arg_index + 1
