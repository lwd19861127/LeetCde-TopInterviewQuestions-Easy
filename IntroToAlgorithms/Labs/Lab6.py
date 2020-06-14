""" Primes, GCD, LCM """
import math


def is_prime(n):
    """ Check if n is prime """
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def prim_factorize(n):
    """https://blog.csdn.net/m0_37586991/article/details/79678043"""
    k = 2
    res = []
    if n == 1:
        return res
    while n != k:
        if n % k == 0:
            if len(res) != 0 and res[len(res)-2] == k:
                res[len(res)-1] += 1
            else:
                res.append(k)
                res.append(1)
            n /= k
        else:
            if len(res) == 0 or res[len(res)-2] != k:
                res.append(k)
                res.append(0)
            k += 1
    if len(res) != 0 and res[len(res)-2] == k:
        res[len(res)-1] += 1
    else:
        res.append(k)
        res.append(1)
    return res


def gcd(a, b):
    """ GCD of a and b """
    res = 1
    prim_factorization_a = prim_factorize(a)
    prim_factorization_b = prim_factorize(b)
    _range = min(len(prim_factorization_a), len(prim_factorization_b))
    for i in range(0, _range, 2):

        res *= prim_factorization_a[i] ** min(prim_factorization_a[i+1], prim_factorization_b[i+1])
    return res


def lcm(a, b):
    """ LCM of a and b """
    return a*b / gcd(a, b)


def generate_primes(n):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """
    res = []
    for i in range(2, n):
        if is_prime(i):
            res.append(i)
    return res
