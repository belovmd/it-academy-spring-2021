""" List practice

1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""

# 1 Create list by generator
lst = [str_1 + str_2 for str_1 in ['a', 'b'] for str_2 in ['b', 'c', 'd']]
print(lst)

# 2 Create list by slice
lst_2 = lst[::2]
print(lst_2)

# 3 Create list by generator
lst_3 = [str(digit) + 'a' for digit in range(1, 5)]
print(lst_3)

# 4 Apply pop method and print element
print(lst_3.pop(1))

# 5 Copy and add element
copy_lst = lst_3[:]
copy_lst.append('2a')
print(copy_lst, lst_3)
