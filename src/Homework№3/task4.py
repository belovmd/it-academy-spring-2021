"""Пары элементов

Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

import random

# Создаем список чисел для входных данных
# lst = list(str(random.randint(10000000, 99999999)))
# lst = [int(num) for num in lst]
lst = [random.randint(-10, 10) for num in range(15)]
print('Входные данные: ', lst)

counted_numbers = []
pairs = []

# Считаем количество повторяющихся элементов
for num in lst:
    if num not in counted_numbers:
        counted_numbers.append(num)
        pairs.append(lst.count(num))
    else:
        pass

# Суммируем все пары и выводим значение
sum_numbers = sum([(num * (num - 1)) / 2 for num in pairs])
print('Количество пар: ', int(sum_numbers))
