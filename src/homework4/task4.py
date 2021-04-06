"""Даны два списка чисел.

Посчитайте, сколько различных чисел входит только в один из этих списков
"""


def count_uniq_num(lst1, lst2):
    """ Function count different numbers in both lists """
    return len(set(lst1) ^ set(lst2))


print(count_uniq_num([1, 2, 3, 4], [3, 4, 5, 6, 7]))
print(count_uniq_num([0, 1, 2], [0, 1, 2]))
