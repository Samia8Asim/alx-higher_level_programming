#!/usr/bin/python3
"""obj from json file module"""


def load_from_json_file(filename):
    """func to create obj from json file
    Args:
        filename: name of file
    """
    import os
    import json
    if os.path.exists(filename):
        with open(filename, encoding='utf-8') as fj:
            obj = json.load(fj)
            return obj
    else:
        return None
