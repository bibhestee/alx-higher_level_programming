#!/usr/bin/python3
"""
   module of a function that reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """
       read_file - read file
       Args:
            filename (file): file to be read
    """
    with open(filename, encoding="UTF-8") as File:
        print(File.read(), end="")
