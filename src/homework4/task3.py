"""Даны два списка чисел.

Посчитайте, сколько различных чисел содержится одновременно как в первом списке,
так и во втором.
"""


def count_num(lst1, lst2):
    """Function count different numbers in both lists """
    return len(set(lst1 + lst2))


# testing
print(count_num([1, 2, 3, 4], [3, 4, 5, 6]))
print(count_num([0, 1, 2], [0, 1, 2]))
