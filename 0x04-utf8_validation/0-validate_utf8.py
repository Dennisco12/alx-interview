#!/usr/bin/python3
"""This determines if a given set of data represent a valid
utf-8 encoding"""


def validUTF8(data):
    """data is a list of integers
    function returns True if data is a valid utf8
    otherwise returns False"""
    count = 0
    for item in data:
        if count == 0:
            if item >> 3 == 0b11110:
                count = 3
            elif item >> 4 == 0b1110:
                count = 2
            elif item >> 5 == 0b110 or item >> 5 == 0b1110:
                count = 1
            elif item >> 7 == 0b1:
                return False
        else:
            if item >> 6 != 0b10:
                return False
            count -= 1
    return count == 0
