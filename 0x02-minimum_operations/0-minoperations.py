#!/usr/bin/python3

"""In a text file, there is a single character H. Your text
editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result
in exactly n H characters in the file."""


def minOperations(n):
    """This is solved by copy and paste when
    the current len is divisible by n or just paste
    when the current length is not divisible by n"""

    text = "H"
    clipboard = ''
    operations = 0

    while len(text) < n:
        if n % len(text) == 0:
            clipboard = text
            text += clipboard
            operations += 2
        else:
            text += clipboard
            operations += 1
    if len(text) != n:
        return 0
    return operations
