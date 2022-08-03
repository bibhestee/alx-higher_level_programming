#!/usr/bin/python3
"""
    Module to create a function that returns a json string
       from an object file
"""


def from_json_string(my_str):
    """
        from_json_string - create a json string from an object
        Args:
             my_str (object): The object
        Return:
             Json string
    """
    import json
    return json.loads(my_str)
