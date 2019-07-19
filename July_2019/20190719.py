# Given a list of integers,
# write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13,
# since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

test = [2, 4, 6, 2, 5]


def max_non_adj(check_list):  # my best attempt, doesn't quite get there.
    """
    this function returns the largest sum of non-adjacent items in list.
    :param check_list:
    :return:
    """
    sum_list = []

    for i in range(len(check_list)):
        list_max = max(range(len(check_list))) + 1
        indexs = []
        for item in range(i, list_max, 2):
            indexs.append(item)
        nonadj_sum = sum([check_list[i] for i in indexs])
        sum_list.append(nonadj_sum)

    return max(sum_list)
