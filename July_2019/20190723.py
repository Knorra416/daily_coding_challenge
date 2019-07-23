# Given an integer k and a string s,
# find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def dist_substring(string, distinct_char):
    """
    this function takes a string and a number of distinct characters and returns the longest substring
    which has the number of unique characters.
    :param string: (string) string to check.
    :param distinct_char: (int) number of distinct characters for substring.
    :return: (string) the longest substring with the correct number of distinct chars.
    """
    distinct_list = list(set(string))

    if len(distinct_list) == distinct_char:
        return string
    else:
        start = 0
        subset = distinct_list[start:distinct_char]
        









