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


# Solution
from random import uniform
from math import pow


def generate():
    return uniform(-1, 1), uniform(-1, 1)


def is_in_circle(coords):
    return coords[0] * coords[0] + coords[1] * coords[1] < 1


def estimate():
    iterations = 10000000
    in_circle = 0
    for _ in range(iterations):
        if is_in_circle(generate()):
            in_circle += 1
    pi_over_four = in_circle / iterations
    return pi_over_four * 4

