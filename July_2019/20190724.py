# The area of a circle is defined as πr^2.
# Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.
import numpy as np


def pi_estimate(x, y, a):
    """
    estimates pi to 3 decimal places
    :param x:
    :param y:
    :param a:
    :return:
    """
    r_sq = x ^ 2 + y ^ 2
    pi = a/r_sq

    return pi




