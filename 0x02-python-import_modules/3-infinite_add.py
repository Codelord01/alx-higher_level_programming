#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg_len = len(sys.argv)
    arg_index = 1
    arg_sum = 0
    while arg_len - 1 > 0:
        arg_sum += int(sys.argv[arg_index])
        arg_index += 1
        arg_len -= 1
    print(arg_sum)
