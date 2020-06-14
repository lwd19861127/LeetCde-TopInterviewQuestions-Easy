#!/usr/bin/python3

# The Sieve of Eratosthenes: To generate a list of prime numbers


def sieve_of_eratosthenes(n):
    """
    Create a boolean list prime[0...n] and initialize
    all entries as True. A value in prime[i] will
    finally be false if i is not a prime, else true.

    :param n: # of elements in List
    :return: list of primes
    """
    prime = [True] * (n + 1)
    prime[0] = False  # 0 is not a prime
    prime[1] = False  # 1 is not a prime
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False

        p += 1

    return prime


if __name__ == '__main__':
    prime_list = sieve_of_eratosthenes(100)
    # enumerate(list) will return a list of pairs (index, element)
    for x, e in enumerate(prime_list):
        if e:
            print(x)
