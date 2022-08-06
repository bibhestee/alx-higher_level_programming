"""
   Module to create a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
       Rectangle - Rectangle class
       Attribute:
                __width (int): width of the rectangle
                __height (int): height of the rectangle
                __x (int): x
                __y (int): y
       Args:
           width: width of the rectangle
           height: height of the rectangle
           x: co-ordinate x
           y: co-ordinate y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
