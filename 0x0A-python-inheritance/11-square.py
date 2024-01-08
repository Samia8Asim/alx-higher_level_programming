#!/usr/bin/python3
"""Square module"""


Rectangle = __import__(f'9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
