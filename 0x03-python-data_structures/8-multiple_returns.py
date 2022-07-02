#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    ch = sentence[0]
    if sentence == '':
        tuple = (None)
    else:
        tuple = (length, ch)
    return tuple
