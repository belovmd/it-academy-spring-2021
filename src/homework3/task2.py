# List practice
# Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
# Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.

import copy

lst_1 = [smbl_lst_1 + smbl_lst_2 for smbl_lst_1 in ['a', 'b'] for smbl_lst_2 in 'bcd']
print(lst_1)
lst_2 = lst_1[0:6:2]
print(lst_2)
lst_3 = [str(i) + 'a' for i in '1234']
print(lst_3)
print(lst_3.pop(1))
lst_4 = copy.deepcopy(lst_3)
lst_4.append('2a')
lst_4.sort()
print(lst_4)
