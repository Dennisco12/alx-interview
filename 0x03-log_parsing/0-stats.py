#!/usr/bin/python3
"""This reads stdin line by line and computes metrics"""
import sys


statusCodes = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
count = 0
totalSize = 0

try:
    args = sys.stdin
    for line in args:
        line_args = line.split(" ")
        if len(line_args) < 5:
            print("Insufficient variables")
            raise TypeError
        fileSize = int(line_args[-1])
        status = line_args[-2]
        if status not in statusCodes:
            print("{} not valid".format(status))
            raise TypeError
        statusCodes[status] += 1
        totalSize += fileSize
        count += 1

        if count == 10:
            print("File size: {}".format(totalSize))
            for key, val in sorted(statusCodes.items()):
                if val != 0:
                    print("{}: {}".format(key, val))
            count = 0
except (KeyboardInterrupt, TypeError):
    pass
finally:
    print('File size: {}'.format(totalSize))
    for key, val in sorted(statusCodes.items()):
        if val != 0:
            print('{}: {}'.format(key, val))
