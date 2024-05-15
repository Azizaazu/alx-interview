#!/usr/bin/python3
""" Prime Game """


def is_prime(n):
    """ Determines the winner
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_count(n):
    primes = [0] * (n + 1)
    count = 0
    for i in range(2, n + 1):
        if primes[i] == 0 and is_prime(i):
            count += 1
            for j in range(i, n + 1, i):
                primes[j] = 1
    return count

def isWinner(x, nums):
    wins_maria = 0
    wins_ben = 0
    for n in nums:
        prime_count_n = prime_count(n)
        if prime_count_n % 2 == 0:
            wins_ben += 1
        else:
            wins_maria += 1
    if wins_maria == wins_ben:
        return None
    return "Maria" if wins_maria > wins_ben else "Ben"

print("Winner:", isWinner(3, [4, 5, 1]))  # Output: Ben
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))  # Output: Maria
