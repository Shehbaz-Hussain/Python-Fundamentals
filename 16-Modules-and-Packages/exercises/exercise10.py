"""Define a function that returns the mean of a list of scores."""

import statistics


def average_score(scores):
    return statistics.mean(scores)


print(average_score([78, 84, 91]))
