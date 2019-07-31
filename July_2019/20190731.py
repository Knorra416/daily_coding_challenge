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






