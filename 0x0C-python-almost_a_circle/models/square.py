"""
   module to create a square class from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
       Square - Square class
                __width (int): width of the square
                __height (int): height of the square.
                __x (int): x.
                __y (int): y.
                size (int): size of the square
                           NB: size = height = width
                area(): calculate area of the square.
                display(): print the square with #.
                __str__(): [Square] (<id>) <x>/<y> - <size>
                update(): updates the value of id, width, height, x and y
                            with args, otherwise kwargs.
       Args:
           width: width of the square.
           height: height of the square.
           x: co-ordinate x.
           y: co-ordinate y.
       Raises:
           TypeError: <name of the attribute> must be an integer.
           ValueError: <name of the attribute> must be > 0.
           ValueError: <name of the attribute> must be >= 0.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints string when instance is called by name """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
