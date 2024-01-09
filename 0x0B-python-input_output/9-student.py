#!/usr/bin/python3
"""student obj module"""


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        json_dic = {}
        for key, val in self.__dict__.items():
            if isinstance(val, (str, int)):
                json_dic[key] = val
        return json_dic
