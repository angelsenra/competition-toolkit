from math import sqrt
from itertools import count
from collections import Counter


def sixn(m):
    """Yields values in the form of 6n - 1 and 6n + 1 until m"""
    if m <= 2:
        return ()
    if m > 2:
        yield 2
    if m > 3:
        yield 3
    for n in count(1):
        x = 6 * n - 1
        y = x + 2
        if x < m:
            yield x
        else:
            break
        if y < m:
            yield y
        else:
            break


def primes(m):
    """Yields primes until m"""
    if m <= 2:
        return ()
    sieve = [True] * m
    for i in sixn(m):
        if sieve[i]:
            yield i
            for mult in range(i * i, m, i):
                sieve[mult] = False


def factors(n):
    """Returns all the factors of a number (including itself)"""
    f = [n]
    if n < 4:
        return f
    for i in primes(n):
        while n != 1:
            if n % i:
                break
            else:
                n //= i
                f.insert(-1, i)
    return f


def gcd(a, b):
    """Greatest common divisor"""
    fa = Counter(factors(a))
    fb = Counter(factors(b))
    out = []
    for i in set(fa) & set(fb):
        out.extend([i] * min(fa[i], fb[i]))
    return out


def lcm(a, b):
    """Least common multiple"""
    fa = Counter(factors(a))
    fb = Counter(factors(b))
    out = []
    for i in set(fa) | set(fb):
        out.extend([i] * max(fa[i], fb[i]))
    return out


def prod(iterable):
    """sum() for multiplication"""
    out = 1
    for i in iterable:
        out *= i
    return out


def is_prime(n):
    if n < 2:
        return False
    return factors(n) == [n]


def goldbachs(n):
    """Every even number can be expressed as the sum of 2 primes"""
    p = list(primes(n))
    for i in p:
        if n - i in p:
            yield i


# Tests
for i in range(10, 50):
    if is_prime(i):
        print("Number %d is prime" % i)
    else:
        print("Number %d:" % i)
        if not i & 1:
            print(list(goldbachs(i)))
        print("factors:", factors(i))
print(gcd(50, 25))
print(lcm(50, 28))
