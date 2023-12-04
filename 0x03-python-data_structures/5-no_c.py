#!/usr/bin/env python3

def no_c(my_string):
    copy = ""

    for ch in my_string:
        if (ch != 'c' and ch != 'C'):
            copy += ch
    return copy
