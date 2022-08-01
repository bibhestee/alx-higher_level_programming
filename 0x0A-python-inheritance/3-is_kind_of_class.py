#!/usr/bin/python3
"""
    Module to check if object is an instance of a specified class
"""

def is_kind_of_class(obj, a_class):
    """
      is_kind_of_class - returns true or false if the object is an instance
       of,or if the object is an instance of a class that inherited
       specified class, otherwise False
      Attributes:
          obj (object) : object
          a_class (class): class
    """
    if isinstance(obj, a_class):
        return True
    elif issubclass(a_class , type(obj)):
        return True
    else:
        return NULL
