#!/usr/bin/env python3

def no_c(my_string):
    copy = ""

    for ch in range(len(my_string)):
        if (my_string[ch] != "c" and my_string[ch] != "C"):
            copy += my_string[ch]
    return copy
