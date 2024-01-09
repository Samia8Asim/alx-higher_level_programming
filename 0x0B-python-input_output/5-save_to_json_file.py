#!/usr/bin/python3
"""json file module"""


def save_to_json_file(my_obj, filename):
    """func save to json file
    Args:
        my_obj: py obj
        filename: name of file
    """
    import json
    with open(filename, 'w', encoding='utf-8') as fj:
        json.dump(my_obj, fj, ensure_ascii=False)
