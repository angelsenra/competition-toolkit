#! python3
import collections
import functools
import itertools
import math
import operator


def multiplicate(l):
    """Same as sum() but using multiplication.
    multiplicate([5, 4, 3, 2, 1]) = 120"""
    return functools.reduce(operator.mul, l, 1)


def fact(n):
    """
    Factorial. fact(5) = 5! = 5 * 4! = 5 * 4 * 3 * 2 * 1 = 120

    :param int n: Target number
    :returns: n!
    :rtype: int
    """
    if n == 1:
        return 1
    return n * fact(n - 1)


def sixn(m):
    """
    Yields numbers of the form 6n + 1 and 6n - 1
    All primes are of the form 6n + 1 or 6n - 1

    :param int m: Upper limit
    :returns: Numbers of the form 6n + 1 and 6n - 1
    :rtype: int
    """
    yield from range(2, min(m, 4))
    for i in range(6, m - 1, 6):
        yield from (i - 1, i + 1)
    try:
        if i + 5 < m:
            yield i + 5
    except NameError:
        if 5 < m:
            yield 5


def is_prime(n):
    """
    Returns whether n is prime or not

    :param int n: Target number
    :returns: Whether is prime or not
    :rtype: bool
    """
    return n > 1 and all(n % i for i in sixn(int(math.sqrt(n)) + 1))


def primes_until(m):
    """
    Returns primes until m
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    :param int m: Upper limit
    :returns: Primes
    :rtype: list[bool]
    """
    sieve = [True] * m
    for i in sixn(int(math.sqrt(m)) + 1):
        if sieve[i]:
            for mult in range(i * i, m, i):
                sieve[mult] = False
    return sieve


def prime_generator():
    """
    Yields primes until infinite

    :returns: Primes
    :rtype: int
    """
    prev_primes = collections.deque([2, 3])
    yield from prev_primes
    x = 5
    for i in itertools.cycle((2, 4)):
        is_prime_var = True
        limit = int(math.sqrt(x)) + 1
        for j in prev_primes:
            if j > limit:
                break
            if not x % j:
                is_prime_var = False
                break
        if is_prime_var:
            prev_primes.append(x)
            yield x
        x += i


def factors(n, include_n=False):
    """
    Returns a list of factors of number n

    :param int n: Target number
    :returns: Factors
    :rtype: list[int]
    """
    fac = []
    for i in sixn(int(math.sqrt(n)) + 1):
        while not n % i:
            fac.append(i)
            n //= i
    if n != 1 and include_n:
        fac.append(n)
    return fac


def factors_until(m):
    """
    Returns a list of sets of the factors of numbers [1, m]
    Themselves not included

    :param int m: Upper limit
    :returns: Factors
    :rtype: list[set[int]]
    """
    sieve = [set() for _ in range(m)]
    for i in sixn(int(math.sqrt(m)) + 1):
        if not sieve[i]:
            for mult in range(i * i, m, i):
                sieve[mult].add(i)
    return sieve


cached_fact = functools.lru_cache(maxsize=None)(fact)
cached_is_prime = functools.lru_cache(maxsize=None)(is_prime)
