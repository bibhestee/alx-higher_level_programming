#!/usr/bin/python3
"""
   module of a function that appends to a text file
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
       append_write - append to a file
       Args:
            filename (file): file to be write to
            text (str): string
    """
    with open(filename, 'a', encoding="utf-8") as File:
        return File.write(text)
