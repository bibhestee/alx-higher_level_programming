#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Check First tuple
    if len(tuple_a) > 0 and len(tuple_a) < 2:
        b = 0
        a = tuple_a[0]
    elif len(tuple_a) < 1:
        a, b = 0, 0
    else:
        a, b = tuple_a

    # Check Second tuple
    if len(tuple_b) > 0 and len(tuple_b) < 2:
        d = 0
        c = tuple_b[0]
    elif len(tuple_b) < 1:
        c, d = 0, 0
    else:
        c, d = tuple_b

    # Return new tuple
    return (a + c, b + d)
