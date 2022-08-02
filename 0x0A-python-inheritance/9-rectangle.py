#!/usr/bin/python3
"""
   module to create a rectangle from base geometry
"""


class BaseGeometry:
    """
       BaseGeometry (class): create a geometry
       Attributes:
           area(): raise exception
       Raises:
           TypeError: <name> must be an integer
           ValueError: <name> must be greater than 0
           Exception: area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return True


class Rectangle(BaseGeometry):
    """
       Rectangle (class): create a rectangle from base geometry
       Attributes:
           area(): raise exception
           integer_validator(): validate the input
       Args:
           width (private): width of the rectangle
           height (private): height of the rectangle
    """
    def __init__(self, width, height):
        if self.integer_validator("width", width) \
           and self.integer_validator("height", height):
            self.__width = width
            self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
