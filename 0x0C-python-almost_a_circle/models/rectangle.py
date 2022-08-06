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
                area(): calculate area of the rectangle
                display(): print the retangle with #
       Args:
           width: width of the rectangle
           height: height of the rectangle
           x: co-ordinate x
           y: co-ordinate y
       Raises:
           TypeError: <name of the attribute> must be an integer
           ValueError: <name of the attribute> must be > 0
           ValueError: <name of the attribute> must be >= 0
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ prints out the rectangle with character # """
        for i in range(0, self.__height):
            print("#" * self.__width)
