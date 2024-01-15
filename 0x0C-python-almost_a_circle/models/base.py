#!/usr/bin/python3
"""base class module"""
import json
import os


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        fname = cls.__name__ + ".json"
        jstr = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        with open(fname, 'w') as fh:
            fh.write(jstr)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        else:
            raise NotImplementedError(
                    f"Class {cls.__name__} not supported in "
                    "create method")
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        fname = cls.__name__ + ".json"
        if not os.path.exists(fname):
            return []
        with open(fname, 'r') as fh:
            jdata = fh.read()
        dict_list = cls.from_json_string(jdata)
        instances = [cls.create(**d) for d in dict_list]
        return instances
