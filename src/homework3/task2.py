"""Homework 3 - Task2

List practice
Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий:
['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий
['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
списке этого элемента не было.
"""

# 1 Generate list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
generated_lst = [el1 + el2 for el1 in "ab" for el2 in "bcd"]
print(generated_lst)

# 2 Slice list
print(generated_lst[::2])

# 3 Generate list ['1a', '2a', '3a', '4a']
generated_lst2 = [str(el3) + "a" for el3 in "1234"]
print(generated_lst2)

# 4 Pop list
print(generated_lst2.pop(1))

# 5 Copy and change list
modified_lst = list.copy(generated_lst2)
modified_lst.insert(1, "2a")
print(generated_lst2)
print(modified_lst)
