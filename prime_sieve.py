#!/usr/bin/env python3
"""prime_sieve - Prime number sieve and utilities."""
import sys, math

def sieve(n):
    if n<2: return []
    s=[True]*(n+1); s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i,v in enumerate(s) if v]

def is_prime(n):
    if n<2: return False
    if n<4: return True
    if n%2==0 or n%3==0: return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0: return False
        i+=6
    return True

def factorize(n):
    factors=[]; d=2
    while d*d<=n:
        while n%d==0: factors.append(d); n//=d
        d+=1
    if n>1: factors.append(n)
    return factors

def nth_prime(n):
    count=0; num=1
    while count<n: num+=1; count+=is_prime(num)
    return num

def goldbach(n):
    if n%2!=0 or n<4: return None
    primes=set(sieve(n))
    for p in sorted(primes):
        if n-p in primes: return (p, n-p)

if __name__=="__main__":
    if len(sys.argv)<2: print("Usage: prime_sieve.py <sieve N|check N|factor N|nth N|goldbach N>"); sys.exit(1)
    cmd,n=sys.argv[1],int(sys.argv[2])
    if cmd=="sieve": ps=sieve(n); print(f"{len(ps)} primes up to {n}"); print(" ".join(map(str,ps[-20:])))
    elif cmd=="check": print(f"{n} is {'prime' if is_prime(n) else 'not prime'}")
    elif cmd=="factor": print(f"{n} = {' × '.join(map(str,factorize(n)))}")
    elif cmd=="nth": print(f"Prime #{n} = {nth_prime(n)}")
    elif cmd=="goldbach": r=goldbach(n); print(f"{n} = {r[0]} + {r[1]}" if r else "N/A")
