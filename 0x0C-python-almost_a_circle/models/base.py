"""
   Module to create a base class
"""
from json import dumps, loads


class Base:
    """
       Base - Base class
       Attributes:
                  __nb_objects (int): number of instance
                  id (int): id number of instance
                  to_json_string(): convert dict to JSON string
                  from_json_string(): deserialize JSON string
                  create(): create an instance from dictionary
                  save_to_file(): save JSON string to file
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

    @staticmethod
    def from_json_string(json_string):
        """ Deserialize JSON string """
        if json_string:
            return loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ Create new instance from dictionary """
        # Create a dummy instance in order to use the update method
        r = cls(2, 3, 0, 0)
        r.update(**dictionary)
        return r

    @classmethod
    def save_to_file(cls, list_objs):
        """
           save_to_file - write JSON string representation of list_objs
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
        # Write JSON string to the file(filename)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(j_str)
