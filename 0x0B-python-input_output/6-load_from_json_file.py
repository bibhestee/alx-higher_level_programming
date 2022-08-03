#!/usr/bin/python3
"""
   Module to create object from a json file
"""


def load_from_json_file(filename):
    """
       load_from_json_file - load function
       Args:
           filename (Object): Json file
    """
    import json
    with open(filename, 'r', encoding="utf-8") as f:
        json_file = f.read()
    return json.loads(json_file)
