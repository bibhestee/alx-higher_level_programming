#!/usr/bin/python3
"""
    Module to check if object is an instance of a specified class
"""

def is_same_class(obj, a_class):
    if obj is None:
        return False
    elif a_class is None:
        return False
    else:
        return issubclass(a_class, type(obj))
