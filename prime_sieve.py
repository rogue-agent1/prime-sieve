#!/usr/bin/env python3
"""Prime number utilities. Zero dependencies."""
import math

def sieve(n):
    if n < 2: return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i): is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True

def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: factors[n] = factors.get(n, 0) + 1
    return factors

def nth_prime(n):
    if n == 1: return 2
    count = 1; candidate = 3
    while count < n:
        if is_prime(candidate): count += 1
        if count < n: candidate += 2
    return candidate

def prime_range(a, b):
    return [p for p in sieve(b) if p >= a]

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    print(f"Primes up to {n}: {sieve(n)}")
