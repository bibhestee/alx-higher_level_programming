#!/usr/bin/python3
"""
    Module to lookup available attributes and methods of an object
"""


def lookup(data):
    """ returns the list of attr and methd in data(object) """
    return list(dir(data))
