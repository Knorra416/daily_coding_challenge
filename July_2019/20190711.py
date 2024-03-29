# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


def check_sum(num_list, target):
    """
    return bool if the provided list has two numbers that sum to the target.
    :param num_list: list of ints
    :param target: int
    :return: bool
    """
    for item in range(len(num_list)):
        first_item = num_list[item]
        other_list = item + 1
        for value in num_list[other_list:]:
            if first_item + value == target:
                result = True
                return result
            else:
                result = False

    return result


# SOLUTION
def two_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] + lst[j] == k:
                return True
    return False


# OR
def two_sum(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False
