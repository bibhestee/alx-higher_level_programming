#!/usr/bin/python3
"""
    This script finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ Get lists of integers and return the peak """
    if list_of_integers:
        """
        peak = 0
        for num in list_of_integers:
            if num > peak:
                peak = num
        """
        list_of_integers.sort()
        peak = list_of_integers[-1]
        return peak
    return None
