#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init finction"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.val_pos_int("width", value)
        self.__width = value

    @property
    def height(self):
        """Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.val_pos_int("height", value)
        self.__height = value

    @property
    def x(self):
        """x dem"""
        return self.__x

    @x.setter
    def x(self, value):
        self.val_non_n_int("x", value)
        self.__x = value

    @property
    def y(self):
        """y dem"""
        return self.__y

    @y.setter
    def y(self, value):
        self.val_non_n_int("y", value)
        self.__y = value

    def val_pos_int(self, name, value):
        """pos_int method"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer.".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0.".format(name))

    def val_non_n_int(self, name, value):
        """non_n_int method"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer.".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0.".format(name))

    def area(self):
        """regtangle area"""
        return self.width * self.height

    def display(self):
        """display regtangle"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """update reg"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """reg dict"""
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
            }

    def __str__(self):
        """str reps"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
