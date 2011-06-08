"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import math

FIRST_SIX_PRIMES = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13}

def e_sieve(upper_bound):
    """Uses the Sieve of Eratosthenes to get a list of the primes up to max."""
    primes = []
    candidates = range(2, upper_bound)
    while candidates:
        head = candidates[0]
        #print head
        primes.append(head)
        candidates = [n for n in candidates[1:] if n % head]
    return primes

def problem_7(n):
    if n < 6:
        return FIRST_SIX_PRIMES[n]

    upper_bound = int(n * math.log(n) + n * math.log(math.log(n)))

    primes = e_sieve(upper_bound)
    return primes[n - 1]

if __name__ == '__main__':
    print problem_7(10001)