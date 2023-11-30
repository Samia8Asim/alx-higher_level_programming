#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_list = sys.argv[1:]
    arg_len = len(arg_list)

    if arg_len == 0:
        print("{} arguments.".format(arg_len))

    elif arg_len == 1:
        print("{} argument:".format(arg_len))
        print("1: {}".format(arg_list[0]))

    elif arg_len > 1:
        print("{} arguments:".format(arg_len))
        for i in range(arg_len):
            print("{}: {}".format(i + 1, arg_list[i]))
