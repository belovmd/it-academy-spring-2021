"""Homework 3 - Task 4"""


def pairs_number(lst: list) -> int:
    """Пары элементов

    Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо
    посчитать.
    Входные данные: строка из чисел, разделенная пробелами.
    Выходные данные: количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
    """
    counts = {}
    pairs_sum = 0
    for element in lst:
        counts[element] = counts.get(element, 0) + 1
        pairs_sum += counts[element] - 1
    return pairs_sum


if __name__ == '__main__':
    assert pairs_number([1, 1, 1]) == 3, 'failed!'
    assert pairs_number([1, 1, 1, 1]) == 6, 'failed!'
    assert pairs_number([1, 1, 1, 1, 1]) == 10, 'failed!'
    assert pairs_number([1, 1, 1, 2, 2, 3]) == 4, 'failed!'
    print(pairs_number([1, 1, 1, 2, 2, 3]))
