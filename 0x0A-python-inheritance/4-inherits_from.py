#!/usr/bin/python3
"""
    Module to check if object is an instance of a specified class
"""


def inherits_from(obj, a_class):
    """
       inherits_from - returns true if the object is an instance of a class
            that inherited specified class, otherwise False
      Attributes:
          obj (object) : object
          a_class (class): class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
