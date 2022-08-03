#!/usr/bin/python3
"""
    Module to writes an object to a text file,
        using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
        save_to_json_file - write to a json file from an
                               object
        Args:
             my_str (object): The object
             filename (file): The file to write to.
    """
    import json
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
