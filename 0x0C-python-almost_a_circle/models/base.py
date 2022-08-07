"""
   Module to create base class
"""
from json import dumps


class Base:
    """
       Base - Base class
       Attributes:
                  __nb_objects (int): number of instance
                  id (int): id number of instance
                  to_json_string(): convert dict to json string
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

    def to_json_string(list_dictionaries):
        """ Convert list of dictionaries to JSON string """
        if list_dictionaries:
            return dumps(list_dictionaries)
        else:
            return "[]"
