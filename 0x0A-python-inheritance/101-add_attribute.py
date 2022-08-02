#!/usr/bin/python3
"""
    module for a function that adds attribute to an object
"""


def add_attribute(mc, name, value):
    """
        add_attribute - adds attribute to an object
        Args:
            mc (Object): The object
            name (attribute): The attribute to add to.
            value (value): The value to be added to attribute
    """
    if type(mc) not in [int, tuple, dict, str, list, float]:
        mc.name = value
    else:
        raise TypeError("can't add attribute")
