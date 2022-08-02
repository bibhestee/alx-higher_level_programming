#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
   module to create a rectangle from base geometry
"""


class Rectangle(BaseGeometry):
    """
       Rectangle (class): create a rectangle from base geometry
       Attributes:
    """
    def __init__(self, width, height):
        if self.integer_validator("width", width):
            self.__width = width
        elif self.integer_validator("height", height):
            self.__height = height
        else:
            pass
