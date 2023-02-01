#!/usr/bin/python3
"""This solves the lockbox problem"""
 
def canUnlockAll(boxes):
    """function definition"""

    all_keys = []
    for items in boxes:
        for key in items:
            if key != 0:
                all_keys.append(key)
        if len(items) == 0 and items != boxes[-1]:
            return False
    all_keys = sorted(all_keys)
    for i in range(1, len(boxes)):
        if i not in all_keys:
            return False
    return True
