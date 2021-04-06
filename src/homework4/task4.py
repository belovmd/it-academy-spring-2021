"""Homework 4 - Task 4"""


def symmetric_difference_cardinality(list1: list, list2: list) -> int:
    """Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один
    из этих списков.
    """
    return len(set(list1) ^ set(list2))


if __name__ == '__main__':
    lst1 = [1, 2, 3]
    lst2 = [2, 4, 5]
    print(symmetric_difference_cardinality(lst1, lst2))
