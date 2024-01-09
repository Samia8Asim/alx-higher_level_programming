#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """read file function
    Args:
        filename: name of file
    """
    with open(filename, encoding='utf-8') as fh:
        print(fh.read(), end="")
