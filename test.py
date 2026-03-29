from prime_sieve import sieve, is_prime, factorize, nth_prime, prime_range
assert sieve(10) == [2,3,5,7]
assert sieve(1) == []
assert is_prime(2) and is_prime(97) and not is_prime(1) and not is_prime(4)
assert factorize(60) == {2:2, 3:1, 5:1}
assert factorize(1) == {}
assert nth_prime(1) == 2
assert nth_prime(5) == 11
assert prime_range(10, 30) == [11,13,17,19,23,29]
print("prime_sieve tests passed")
