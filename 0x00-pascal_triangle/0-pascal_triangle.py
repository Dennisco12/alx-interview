#!/usr/bin/python3

"""This function returns the pascal triangle according
to an inputted size"""


def factorial(x):
    """This returns the factorial value of a number"""
    if x == 0:
        return 1
    return x * factorial(x - 1)

def combination(n, r):
    """This returns the combination of the two inputted numbers"""
    comb = factorial(n) // (factorial(n-r) * factorial(r))
    return comb

def pascal_triangle(n):
    """Function definition"""

    if n <= 0:
        return []

    triangle = []
    for idx in range(n):
        row = []
        for count in range(idx + 1):
            row.append(combination(idx, count))
        triangle.append(row)
    return triangle


