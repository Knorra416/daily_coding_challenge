# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.


# Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair
# Implement car and cdr.


def make_list(a, b):
    """
    this function takes two items (pairs) and returns a list
    :param a:
    :param b:
    :return:
    """
    my_list = [a, b]
    return my_list


def car(f):
    """
    this function returns the first element of the pairs provided from a function.
    :param f: function (cons)
    :return: int
    """
    return f(make_list)[0]


def cdr(f):
    """
    this function returns the last element of the pairs provided from a function.
    :param f: function (cons)
    :return: int
    """
    return f(make_list)[1]
