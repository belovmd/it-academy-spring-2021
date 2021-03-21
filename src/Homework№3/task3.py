"""Tuple practice

1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
4. Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно
   выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
"""

# 1. Creating list and making tuple

lst = list('abcd')
tpl = tuple(lst)
print(lst, tpl)

# 2. Creating tuple and making list

tpl = tuple('abcd')
lst = list(tpl)
print(tpl, lst)

# 3. 1 string

a, b, c = 'a', 2, 'python'
print(a, b, c)

# 4. 1 element tuple

tpl = ([1, 2, 3], )
for lst in tpl:
    for element in lst:
        print(element)
if len(tpl) == 1:
    print(True)
else:
    print(False)
