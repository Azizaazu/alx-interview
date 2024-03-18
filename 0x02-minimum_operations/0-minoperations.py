#!/usr/bin/python3

"""
This module contains a function to calculate the minimum number of operations
"""


def minOperations(n):
    """
    Calculate the minimum number of operations
    """
    if n <= 1:
        return 0

    operations = 0
    clipboard = 1
    characters = 1

    while characters < n:
        if n % characters == 0:
            clipboard = characters
            operations += 1

        characters += clipboard
        operations += 1

    return operations
