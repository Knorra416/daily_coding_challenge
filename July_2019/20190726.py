# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log.
# i is guaranteed to be smaller than or equal to N.


def order_id_logging(order_id_list, n, logger):
    """
    This function records order_ids into a log.
    :param order_id_list: list of order_ids
    :param n: int number of n last orders to put into log
    :param logger: logger object
    :return: the nth element from the log
    """
    for i in order_id_list:
        if order_id_list.index(i) <= n:
            record(i)
        else:
            continue

    return get_last(n)


# Solution
class Log(object):
    def __init__(self, n):
        self._log = []
        self.n = n

    def record(self, order_id):
        if len(self._log) >= self.n:
            self._log.pop(0)
        self._log.append(order_id)

    def get_last(self, i):
        return self._log[-i]




