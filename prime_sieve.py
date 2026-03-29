#!/usr/bin/env python3
"""prime_sieve - Prime generation: Sieve of Eratosthenes, Atkin, segmented."""
import sys, json, math

def eratosthenes(n):
    if n < 2: return []
    sieve = [True]*(n+1); sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i): sieve[j] = False
    return [i for i in range(n+1) if sieve[i]]

def segmented_sieve(lo, hi):
    if hi < 2: return []
    lo = max(lo, 2)
    small_primes = eratosthenes(int(hi**0.5)+1)
    sieve = [True]*(hi-lo+1)
    for p in small_primes:
        start = max(p*p, ((lo+p-1)//p)*p)
        for j in range(start, hi+1, p):
            sieve[j-lo] = False
    return [i+lo for i in range(hi-lo+1) if sieve[i]]

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n%2==0 or n%3==0: return False
    i = 5
    while i*i <= n:
        if n%i==0 or n%(i+2)==0: return False
        i += 6
    return True

def prime_factors(n):
    factors = []
    d = 2
    while d*d <= n:
        while n%d == 0: factors.append(d); n //= d
        d += 1
    if n > 1: factors.append(n)
    return factors

def goldbach(n):
    if n <= 2 or n%2: return None
    primes = set(eratosthenes(n))
    for p in sorted(primes):
        if (n-p) in primes: return (p, n-p)
    return None

def main():
    print("Prime sieve demo\n")
    primes = eratosthenes(100)
    print(f"  Primes <= 100: {len(primes)} ({primes[:10]}...)")
    seg = segmented_sieve(1000000, 1000100)
    print(f"  Primes in [1M, 1M+100]: {seg[:5]}... ({len(seg)} total)")
    print(f"  Factors of 2520: {prime_factors(2520)}")
    print(f"  Factors of 1000003: {prime_factors(1000003)}")
    for n in [4, 20, 100]:
        g = goldbach(n)
        print(f"  Goldbach({n}): {g[0]}+{g[1]}" if g else f"  Goldbach({n}): None")
    # Twin primes
    twins = [(p, p+2) for p in eratosthenes(1000) if is_prime(p+2)]
    print(f"  Twin primes < 1000: {len(twins)} pairs, last: {twins[-1]}")

if __name__ == "__main__":
    main()
