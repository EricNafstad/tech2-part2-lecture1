#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:41:16 2024

@author: ericnafstad
"""

"""
Part 2, Lecture 1, Example 1

Implement and test argmax() function that returns the location of a maximum.
"""


def argmax(values):
    """
    Return the location and value of the maximum contained in a given sequence.

    Parameters
    ----------
    values : Sequence of numbers

    Returns
    -------
    imax : int
        Location of the maximum
    vmax : int or float
        Maximum value
    """

    # ADD YOUR IMPLEMENTATION HERE


    N = len(values)
    
    if N == 0:
        raise ValueError('Empty sequences are not supported')
    
    imax = 0
    vmax = values[0]
    
    for i in range(1, N):
        v = values[i]
        if v > vmax:
            imax = i
            vmax = v
    
    return imax, vmax


def main():
    # Create list of values to test argmax()
    values = [2, 3, -1, 7, 4]
    
    # Use argmax() to locate the maximum
    imax, vmax = argmax(values)
    
    # Print the results
    print(f"The maximum value is {vmax} at index {imax}")

    try:
        argmax([])
    except ValueError:
        print('Error encountered')

if __name__ == '__main__':
    main()