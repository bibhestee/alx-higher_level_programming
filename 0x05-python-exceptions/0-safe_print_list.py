#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ele = 0  # Number of elements
    try:
        for n in range(0, x):
            if my_list[n] != my_list[-1] and n != (x - 1):
                print(my_list[n], end="")
            else:
                print(my_list[n])  # Add new line to the last element
            ele += 1
        return x
    except BaseException:
        return ele
