#!/usr/bin/python3
"""square module"""


def print_square(size):
    """func to print square

    Args:
        size: square size
    Raise:
        TypeError: if size not int
        ValueError: if size less than 0
        TypeError: if size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
