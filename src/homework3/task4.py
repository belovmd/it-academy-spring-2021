"""
Пары элементов

Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

input_str = input()
lst = input_str.split()
repetitive = []

for element in lst:
    if lst.count(element) > 1 and element not in repetitive:
        repetitive.append(element)

print(len(repetitive))
