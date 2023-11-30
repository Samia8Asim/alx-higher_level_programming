#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arg = sys.argv[1:]
    leng = len(arg)
    sum = 0

    for i in range(leng):
        sum += int(arg[i])
    print("{}".format(sum))
