"""
   Module to create base class
"""


class Base:
    """
       Base - Base class
       Args:
            id (int): id number of instance
            __nb_objects (int): nb of instance(objects)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
