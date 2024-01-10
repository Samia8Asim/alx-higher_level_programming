#!/usr/bin/python3
"""append module"""


def append_after(filename="", search_string="", new_string=""):
    """
     inserts a line of text to a file
     after a search_string
     """
    if not filename or not search_string or not new_string:
        return
    with open(filename, encoding='utf-8') as file:
        lines = fh.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string + '\n')
        fh.seek(0)
        fh.truncate()
        fh.writelines(lines)
