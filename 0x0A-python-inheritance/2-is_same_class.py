#!/usr/bin/python3
"""
    Module to check if object is an instance of a specified class
"""

def is_same_class(obj, a_class):
    return issubclass(a_class, type(obj))
