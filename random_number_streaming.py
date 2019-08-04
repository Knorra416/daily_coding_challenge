import random


# This is a solution from an email problem!
def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element
