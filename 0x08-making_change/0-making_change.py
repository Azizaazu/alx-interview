#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """ Determines the fewest number of coins
    """
    if total <= 0:
        return 0
    rem = total
    cns_count = 0
    cn_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if cn_idx >= n:
            return -1
        if rem - sorted_coins[cn_idx] >= 0:
            rem -= sorted_coins[cn_idx]
            cns_count += 1
        else:
            cn_idx += 1
    return cns_count
