#!/usr/bin/python3
"""from json module"""


def from_json_string(my_str):
    """from_json_string func
    Args:
        my_str: json string
    Return:
        obj: object represented by a JSON string
    """
    import json
    py_obj = json.loads(my_str)
    return py_obj
