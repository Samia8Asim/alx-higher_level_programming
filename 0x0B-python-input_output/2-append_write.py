#!/usr/bin/python3
"""append module"""


def append_write(filename="", text=""):
    """append to a file
    Args:
        filename: name of file
        text: text to append
    Return:
        int: num of added char
    """
    with open(filename, 'a', encoding='utf-8') as fh:
        fh.write(text)
        return len(text)
