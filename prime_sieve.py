#!/usr/bin/env python3
"""prime_sieve - Prime number algorithms (Sieve of Eratosthenes, Miller-Rabin, factorization)."""
import sys, random

def sieve(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def miller_rabin(n, k=10):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def factorize(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def test():
    primes = sieve(30)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert is_prime(97) and not is_prime(100)
    random.seed(42)
    assert miller_rabin(104729)  # prime
    assert not miller_rabin(104730)
    assert factorize(60) == [2, 2, 3, 5]
    assert factorize(97) == [97]
    assert factorize(1) == []
    print("OK: prime_sieve")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: prime_sieve.py test")
