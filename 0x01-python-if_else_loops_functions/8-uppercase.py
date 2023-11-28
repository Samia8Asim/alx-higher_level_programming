#!/usr/bin/python3
def uppercase(str):
    out_str = ""
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            out_str += "{}".format(chr(ord(str[i]) - ord('a') + ord('A')))
        else:
            out_str += "{}".format(str[i])
    print("{}".format(out_str), end="\n")
