#!/usr/bin/python3

def minOperations(n):
    if n <= 0:
        return 0
    prime_factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        prime_factors.append(n)
    return len(set(prime_factors))
