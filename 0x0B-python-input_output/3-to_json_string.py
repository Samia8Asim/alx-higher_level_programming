#!/usr/bin/python3
"""json string module"""


def to_json_string(my_obj):
    """json string func
    Args:
        my_obj: input obj
    Return:
        str: JSON representation of an obj
    """
    import json
    json_str = json.dumps(my_obj)
    return json_str
