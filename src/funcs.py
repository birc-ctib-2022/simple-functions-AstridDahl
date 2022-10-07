"""Exercises with simple functions"""
from math import sqrt

def prod(a, b, c):
    """
    Compute the product of three numbers.

    >>> prod(1, 2, 3)
    6
    """
    product = a*b*c
    return product

glob_val = 4

def prod2(b):
    """
    Get a global a and write to a local c before computing prod(a, b, c)

    >>> prod2(42)
    a*42*c
    """
    a = glob_val
    c = 2
    product = a*b*c
    return product


def longest(x, y):
    """
    Returning the longest of two lists.

    >>> longest([1, 2, 3], [4, 5])
    [1, 2, 3]
    """
    if len(x) > len(y):
        return x
    elif len(y) > len(x):
        return y
    else:
        return None

    # return x if len(x) > len(y) else y


def dist(p1, p2):
    """
    Compute the distance between p1 and p2.

    >>> dist((1,2), (3,4))
    sqrt(8)
    """
    x1, y1 = p1
    x2, y2 = p2
    
    d = sqrt(abs((x1-x2))**2+abs((y1-y2))**2)

    return d


