#!/usr/bin/python3
"""write to file module"""


def write_file(filename="", text=""):
    """write to file func
    Args:
        filename: name of file
        text: text to write
    Return:
        int: number of char
    """
    with open(filename, 'w', encoding='utf-8') as fh:
        fstr = fh.write(text)
        return fstr
