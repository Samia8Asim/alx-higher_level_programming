#!/usr/bin/python3
"""Square module"""


class Square:
    """Square define"""
    def __init__(self, size=0):
        """Constructor.
        Args:
            size: Square length
        Raises:
            TypeError : If size not integer
            ValueError : If size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
