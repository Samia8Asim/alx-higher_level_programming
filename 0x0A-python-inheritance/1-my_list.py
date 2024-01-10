#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """print sirted list"""
        print(sorted(self))


if __name__ = "__main__":
    import doctest
    doctest.testfile(' tests/1-my_list.txt')
