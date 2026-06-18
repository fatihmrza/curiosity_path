__author__ = "8500551, Mirza"


"""This module includes three algorithm functions for the optimise the specific structure"""


def ratio_value(r1, r2):
    """
        The functions is an optimisation algorithm, which takes 2 Parameter and
        compares them with their own prize, cost through ratio. (ratio1 = prize/cost)
        Whichever larger will be chosen.
        Here is r1,r2 represents (path, cost, prize) which is important for recursion
    >>> ratio_value((['A', 'B'], 5, 6), (['A', 'B'], 8, 9))
    (['A', 'B'], 5, 6)
    >>> ratio_value((['A', 'B'], 5, 6), None)
    (['A', 'B'], 5, 6)
    >>> ratio_value(None, None)

    >>> ratio_value((4,4), (['A', 'B'], 5, 6))
    Traceback (most recent call last):
    ...
    ValueError: not enough values to unpack (expected 3, got 2)
    """
    if r1 is None:
        return r2
    if r2 is None:
        return r1
    x, x1, x2 = r1
    y, y1, y2 = r2
    try:
        ratio1 = x2/x1
        ratio2 = y2/y1
        if ratio1 >= ratio2:
            return r1
        if ratio2 > ratio1:
            return r2
    except ZeroDivisionError:
        if x1 == 0:
            return r1
        return r2


def internal_comparison(p1, p2):
    """
    This function is an optimisation algorithm, which takes 2 Parameter and compares
    them according to firstly prize values. If they are equal then costs.
    Here is p1, p2 represents (path, cost, prize) which is important for recursion.

    >>> internal_comparison((['A', 'B'], 5, 6), (['A', 'B'], 7, 10))
    (['A', 'B'], 7, 10)
    >>> internal_comparison((['A', 'B'], 5, 6), (['A', 'B'], 7, 6))
    (['A', 'B'], 5, 6)
    >>> internal_comparison((['A', 'B'], assert, 6), (['A', 'B'], 9, 10))
    Traceback (most recent call last):
    ...
    SyntaxError: invalid syntax
    """
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    if z1 > z2:
        return p1
    if z1 < z2:
        return p2

    if y1 < y2:
        return p1
    return p2


def score_cal(path, k1=0.35, k2=0.65):
    """
    The function generates a score for a path according to his cost and prize values.
    The cost and values have different weights, which is %35 for cost and %65 for prize.
    :param path: takes two parameters, which can be called from Graph.edges
    :param k1: The weigh of cost.
    :param k2: The weigh of prize
    :return: the score that usable for the comparing of two paths.
    >>> score_cal((5,2))
    -0.44999999999999996
    >>> score_cal((5,2), k1=0.65, k2=0.35)
    -2.55
    >>> score_cal(("on","try"), k1=1)
    Traceback (most recent call last):
    ...
    TypeError: can't multiply sequence by non-int of type 'float'
    """
    cost, prize = path
    cost *= k1
    prize *= k2
    score = prize - cost
    return score


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
