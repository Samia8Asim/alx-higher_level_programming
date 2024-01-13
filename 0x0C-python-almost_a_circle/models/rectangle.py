#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.val_pos_int("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.val_pos_int("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.val_non_n_int("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.val_non_n_int("y", value)
        self.__y = value

    def val_pos_int(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer.".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0.".format(name))

    def val_non_n_int(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer.".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0.".format(name))

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.height):
            print('#' * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
