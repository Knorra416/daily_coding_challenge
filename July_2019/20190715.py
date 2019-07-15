# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.


# Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
# Implement car and cdr.


def car(f):
    """
    this function returns the min of the pairs provided from a function.
    :param f: function (cons)
    :return: int
    """
    return f(min)


def cdr(f):
    """
    this function returns the min of the pairs provided from a function.
    :param f: function (cons)
    :return: int
    """
    return f(max)

# These aren't quite right. Don't catch the case where pairs are not ordered as min/max.

