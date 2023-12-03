#!/usr/bin/env python3

def no_c(my_string):
    copy = ""

    for ch in my_string:
        if ch == "c" or ch == "C":
            continue
        copy += ch
    return copy
