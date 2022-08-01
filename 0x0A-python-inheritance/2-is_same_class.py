#!/usr/bin/python3
"""
    Module to check if object is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
       is_same_class - returns true if obj is an instance of a_class
       Attributes:
           obj(object): The object
           a_class(class): The class
       Return: true if obj is an instance or false is not
    """
    return issubclass(a_class, type(obj))
