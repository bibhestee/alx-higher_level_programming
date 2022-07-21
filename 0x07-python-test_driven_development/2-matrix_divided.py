#!/bin/bash/python3
"""


"""


def matrix_divided(matrix, div):
    """

    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div <= 0:
        raise ZeroDivisionError("division by zero")

    list = []
    for item in matrix:
        new_list = []
        for value in item:
            if type(value) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                x = "{:.2f}".format(value/div)
                new_list.append(x)
        list.append(new_list)
    return list
