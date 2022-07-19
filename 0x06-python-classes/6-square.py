#!/usr/bin/python3
"""
    This module defines a class Square with
    private instances attribute, public instance methods,
    setter and getter to modify private instances and raise exceptions
"""


class Square:

    """
    Square (class): create a square with the size specified by
    the parameter size
    Raise error if type is not int or size is less than zero.
    Print out square with the character # and spaces.

    Attributes:
        size (int): specify the size of the square.
        area(): returns the area of the square.
        my_print(): prints out the square with # character to stdout.
        position (int): specify the position to include space.
    Args:
        size (int): size of the square.
        position (int): position of the spaces.
    Raises:
        ValueError: if size is less than zero(0).
        TypeError: if size is not an integer.
        TypeError: if position is not a tuple of 2 positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        try:
            self.__position = position
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """ :size: returns the private instance. """
        return self.__size

    @size.setter
    def size(self, size):
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ :position: returns the position private instance. """
        return self.__position

    @position.setter
    def position(self, pos):
        try:
            self.__position = pos
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculate area of the square and return the result
        Returns:
            Square area.
        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """ Prints the square with the character # to the stdout. """
        for i in range(0, self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
