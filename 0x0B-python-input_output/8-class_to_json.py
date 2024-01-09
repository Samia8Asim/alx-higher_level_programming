#!/usr/bin/python3
"""class json module"""


def class_to_json(obj):
    """func class_to_json
    Args:
        obj: input obj
    Return:
        dic: description with data structure
    """
    json_dic = {}
    for key, val in obj.__dict__.items():
        if isinstance(val, (list, dict, str, int, bool)):
            json_dic[key] = val
    return json_dic
