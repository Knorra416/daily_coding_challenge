# Given an array of integers,
# return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?
import numpy as np


def prod_array(input_list):
    """
    this function returns the product of a list for all elements except the one at i
    :param input_list:
    :return: list of products
    """
    output_list = []
    for val in range(len(input_list)):
        filtered_list = [x for i, x in enumerate(input_list) if i != val]
        product = np.prod(filtered_list)
        output_list.append(product)

    return output_list
