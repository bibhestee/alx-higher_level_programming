#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ele = 0  # Number of elements
    try:
        for n in range(0, x):
            if my_list[n]:
                if my_list[n] != my_list[-1] and n != (x - 1):
                    print("{:d}".format(my_list[n]), end="")
                    ele += 1
                else:
                    print("{:d}".format(my_list[n]))
                    ele += 1
            else:
                continue
        return ele
    except IndexError:
        return ele
    except BaseException:
        return ele
