#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        i = 0
        for key in a_dictionary:
            if a_dictionary[key] > i:
                result = key
                i = a_dictionary[key]
        return result
