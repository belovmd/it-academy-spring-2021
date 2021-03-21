"""Homework 3 - Task 2

List practice
1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не
   было.
"""

# 1
list1 = [el1 + el2 for el1 in 'ab' for el2 in 'bcd']
print('1.   ', list1)

# 2
list2 = list1[::2]
print('2.   ', list2)

# 3
list3 = [el + 'a' for el in '1234']
print('3.   ', list3)

# 4
print('4.   ', list3.pop(list3.index('2a')))

# 5
list5 = list3[:]
list5.append('2a')
print('5.    original list: {original}   final list: {final}'.format(original=list3, final=list5))
