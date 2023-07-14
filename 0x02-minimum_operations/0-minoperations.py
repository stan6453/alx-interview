#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Given a number n, write a method that calculates the
    fewest number of operations needed to result
    in exactly n H characters in the file.
    """

    if n < 2:
        return 0

    sum_factors = 0
    factor = 1

    while True:
        factor = factor + 1
        if n % factor == 0:
            sum_factors += factor
            n = n/factor
            factor = 1
            if n == 1:
                return sum_factors
