#!/usr/bin/python3
""" Prime Game """


def is_prime(n):
    """ Checks if a number is prime.
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

def isWinner(x, nums):
    """
    Determines the winner of each round of the prime game.
    """
    marias_wins = 0
    for n in nums:
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            marias_wins += 1

    if marias_wins > x // 2:
        return "Ben"
    elif marias_wins < x // 2:
        return "Maria"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
