#!/usr/bin/python3
"""
   module of a function that writes to a text file
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
       write_file - write to a file
       Args:
            filename (file): file to be write to
            text (str): string
    """
    with open(filename, 'w', encoding="utf-8") as File:
        return File.write(text)
