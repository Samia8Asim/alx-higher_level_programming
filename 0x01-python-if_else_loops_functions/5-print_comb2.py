#!/usr/bin/python3
for i in range(100):
    if 0 <= i <= 98:
        print("{:02}, ".format(i), end="")
    elif i == 99:
        print("{:02}".format(i))
