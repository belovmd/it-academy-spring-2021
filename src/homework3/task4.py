"""Homework 3 - Task 4"""


from math import factorial


def pairs_number(lst: list) -> int:
    """Пары элементов

    Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо
    посчитать.
    Входные данные: строка из чисел, разделенная пробелами.
    Выходные данные: количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
    """
    ret_val = 0
    elements_counts = {}
    for element in lst:
        elements_counts[element] = elements_counts.get(element, 0) + 1
    for count in elements_counts.values():
        if count > 1:
            ret_val += combinations_without_repetitions(count, 2)
    return ret_val


def combinations_without_repetitions(n: int, k: int) -> int:
    """Число сочетаний без повторений из n по к

    Генерирует исключение ValueError, если n < k.
    """
    if n < k:
        raise ValueError('n < k')
    return int(factorial(n) / (factorial(n - k) * factorial(k)))


if __name__ == '__main__':
    assert pairs_number([1, 1, 1]) == 3, 'failed!'
    assert pairs_number([1, 1, 1, 1]) == 6, 'failed!'
    print(pairs_number([1, 1, 1, 2, 2, 3]))
