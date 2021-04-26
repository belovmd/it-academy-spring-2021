import collections


"""
Пары элементов

Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def pairs(str_):
    counter_ = collections.Counter(str_.split())
    num_of_pairs = 0
    for x in counter_.values():
        num_of_pairs += x * (x - 1) // 2
    return num_of_pairs


assert pairs('1 1 1') == 3, 'Should be 3!'
assert pairs('1 1 1 2 2 2 2') == 9, 'Should be 9!'
assert pairs('1 1 1 1') == 6, 'Should be 6!'
