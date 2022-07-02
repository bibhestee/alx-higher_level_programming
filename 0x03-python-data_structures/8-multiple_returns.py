#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    ch = sentence[0]
    if len(sentence) < 1:
        tuple = (length, None)
    else:
        tuple = (length, ch)
    return tuple
