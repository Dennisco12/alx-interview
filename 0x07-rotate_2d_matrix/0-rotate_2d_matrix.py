#!/usr/bin/python3
""" Given an nxn matrix, rotate it 90 degrees
clockwise"""


def rotate_2d_matrix(matrix):
    """Returns nothing"""
    n = len(matrix)
    temp = []
    for i in range(n):
        j = n - 1
        new = []
        while j >= 0:
            new.append(matrix[j][i])
            j -= 1
        temp.append(new)
    for k in range(len(temp)):
        matrix[k] = temp[k]
