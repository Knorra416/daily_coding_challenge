# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def min_classrooms(class_times):
    """
    given a list of (start,end) arrays return the min number of rooms required to meet the intervals.
    :param class_times:
    :return:
    """
    total_rooms = 1
    list_schedule = []
    for index, interval in enumerate(class_times):
        start = interval[0]
        end = interval[1]
        diff = end - start

    return list_schedule


# Solution
def overlaps(a, b):
    start_a, end_a = a
    start_b, end_b = b
    # It doesn't overlap if it's like this:
    #   |start_a .... end_a|  <---> |start_b ... end_b|
    # or like this:
    #   |start_b .... end_b|  <---> |start_a ... end_a|
    # so return not or either of these
    return not (end_a < start_b or start_a > end_b)


def max_overlapping(intervals):
    current_max = 0
    for interval in intervals:
        num_overlapping = sum(overlaps(interval, other_interval)
                              for other_interval in intervals
                              if interval is not other_interval)
        current_max = max(current_max, num_overlapping)
    return current_max




