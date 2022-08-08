"""
   Module to create a base class
"""
from json import dumps


class Base:
    """
       Base - Base class
       Attributes:
                  __nb_objects (int): number of instance
                  id (int): id number of instance
                  to_json_string(): convert dict to json string
                  save_to_file(): save json string to file
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert list of dictionaries to JSON string """
        if list_dictionaries:
            return dumps([item for item in list_dictionaries])
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
           save_to_file - write json string representation of list_objs
                          to a file
        """
        if list_objs:
            # Convert the instances to a dictionary
            dict = [item.to_dictionary() for item in list_objs]
        else:
            dict = []
        # Serialize the list of dictionaries
        j_str = cls.to_json_string(dict)
        # Get filename from instance magic method
        filename = cls.__name__ + ".json"
        # Write json string to the file(filename)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(j_str)
