#!/usr/bin/python3
"""
Define isWinner func, a solution to the Prime Game Problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n include
    Args:
    n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Ben = Maria = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Maria += 1
        else:
            Ben += 1
        if Ben > Maria:
            return 'Ben'
        if Maria > Ben:
            return 'Maria'
        return None
