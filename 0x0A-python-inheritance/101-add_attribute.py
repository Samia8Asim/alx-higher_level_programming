#!/usr/bin/python3
"""add attribute func module"""


def add_attribute(obj, name, value):
    """add attribute func"""
    if isinstance(obj, object):
        obj.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
