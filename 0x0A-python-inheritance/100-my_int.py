"""
    module to create MyInt to inherit from int
"""


class MyInt(int):
    """
        MyInt - inherit from int but reverse equal
                and not equal result
        Attributes:
            __str__: returns the input value
            __eq__ :  returns false if equal
            __ne__ :  returns true if not equal
        Arg:
            value (int): value passed as argument
    """
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return "{}".format(self.__value)

    def __eq__(self, other):
        if other:
            return False

    def __ne__(self, other):
        if other:
            return True
