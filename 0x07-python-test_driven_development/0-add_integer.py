#!/usr/bin/python3

#0-add_integer.py

"""module with add function"""


def add_integer(a, b=98):
    """function that adds two numbers

    Parameters:
    - a: first num
    - b: second num

    Return:
    int: sum of the two numbers

    Raises:
    TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, float):
        a = int(a)
    result = a + b

    return result
