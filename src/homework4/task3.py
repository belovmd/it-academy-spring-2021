"""Homework 4 - Task 3"""


def intersection_cardinality(list1: list, list2: list) -> int:
    """Мощность множества

    Даны два списка чисел. Посчитайте, сколько различных чисел содержится одновременно
    как в первом списке, так и во втором.
    """
    return len(set(list1) & set(list2))


if __name__ == '__main__':
    lst1 = [1, 2, 3]
    lst2 = [2, 4, 5]
    print(intersection_cardinality(lst1, lst2))
