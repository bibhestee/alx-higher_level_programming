#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    # Reverse the list
    my_list.reverse()
    # Loop through the list
    for item in my_list:
        print("{}".format(item))
