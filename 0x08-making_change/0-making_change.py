#!/usr/bin/python3
"""Making change module"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total."""
    if total <= 0:
        return 0
    change = [total+1] * (total+1)
    change[0] = 0
    for money in range(1, len(change)):
        for coin in coins:
            if money-coin >= 0:
                change[money] = min(change[money-coin] + 1, change[money])
    return change[-1] if change[-1] != (total+1) else -1
