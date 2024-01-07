#!/usr/bin/python3
"""text module"""


def text_indentation(text):
    """ func to prints a text with 2 lines

    Args:
        text: input text
    Raise:
        TypeError: if text not str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    trig_char = ['?', '.', ':']
    line = ""

    for ch in text:
        line += ch

        if ch in trig_char:
            print(line.strip() + '\n')
            line = ""

    if line.strip():
        print(line.strip())


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
