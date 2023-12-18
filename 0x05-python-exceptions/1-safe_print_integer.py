#!/usr/bin/python3

def safe_print_integer(value):
    try:
        int_val = int(value)
        print("{:d}".format(int_val))
        return True
    except ValueError:
        return False
