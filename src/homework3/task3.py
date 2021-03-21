"""Homework 3 - Task 3

Tuple practice
1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
4. Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно
   выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.

"""


# 1
list1 = ['a', 'b', 'c']
tuple1 = tuple(list1)
print('1.   ', tuple1)

# 2
tuple2 = ('a', 'b', 'c')
list2 = list(tuple2)
print('2.   ', list2)

# 3
a, b, c = 'a', 2, 'python'
print('3.    a = {}; b = {}; c = {}'.format(a, b, c))

# 4
tuple4 = ([1, 2, 3],)
print("4.    tuple's first element length = ", len(tuple4))
for index, value in enumerate(tuple4[0]):
    print("      iter{} on tuple's first element: {}".format(index, value), sep=' ')
