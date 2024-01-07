#!/usr/bin/python3
""""say my name module"""


def say_my_name(first_name, last_name=""):
    """function to print names

    Args:
        first_name: first_name
        last_name: last_name

    Raise:
        TypeError if first or last names not str.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
