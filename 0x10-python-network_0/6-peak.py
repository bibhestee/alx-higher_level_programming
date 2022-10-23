#!/usr/bin/python3
"""
    This script finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ Get lists of integers and return the peak """
    if list_of_integers:
        nums = len(list_of_integers)
        peak = 0
        for i in range(nums):
            if list_of_integers[i] > peak:
                peak = list_of_integers[i]
        return peak
    return None
