# Given the mapping a = 1, b = 2, ... z = 26,
# and an encoded message,
# count the number of ways it can be decoded.

# For example,
# the message '111' would give 3,
# since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable.
# For example, '001' is not allowed.

mapping = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def decoder(message, mapping):
    """
    this function returns the count of
    :param message:
    :return:
    """
    decoded_options = []
    for i in range(len(message)):
        remaining = [y for x, y in enumerate(message) if x != i]
        remaining = ''.join(remaining)
        if len(remaining) < 3:
            decode = mapping[int(message[i])-1] + mapping[int(remaining)-1]
            decoded_options.append(decode)
        else:
            continue

    return len(decoded_options), decoded_options


# Solution
def num_encodings(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1: # This covers empty string
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += num_encodings(s[2:])

    total += num_encodings(s[1:])
    return total
