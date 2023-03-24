#!/usr/bin/python3

"""my solution"""


def makeChange(coins, total):
    """My solution"""
    if total <= 0:
        return 0

    rem = total
    idx = len(coins) - 1
    count = 0
    coins = sorted(coins)

    while rem > 0:
        if idx < 0:
            return -1
        if rem - coins[idx] >= 0:
            rem -= coins[idx]
            count += 1
        else:
            idx -= 1

    return count
