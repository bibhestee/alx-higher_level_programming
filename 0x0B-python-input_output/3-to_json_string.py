#!/usr/bin/python3
import json
"""
    Module of a function that returns JSON
     representation of an object(string)
"""


def to_json_string(my_obj):
    """
        to_json_string - encode to JSON rep
        Args:
            my_obj (str): The object
        Return:
              a json string representation
    """
    return json.dumps(my_obj)
