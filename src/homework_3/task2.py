# Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].

# my_list = []
# lst1 = ['a', 'b']
# lst2 = ['b', 'c', 'd']
# for i in lst1:
#     for j in lst2:
#         my_list.append(i+j)
# print(my_list)

my_list = [i + j for i in ['a', 'b'] for j in ['b', 'c', 'd']]
print(my_list)

# Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].

print(my_list[::2])

# Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a']

my_list = [str(i) + 'a' for i in range(1, 5)]
print(my_list)

# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.

print(my_list.pop(1))

# Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого
# элемента не было.

my_list2 = []
my_list2 = my_list.copy()
my_list2.insert(1, '2a')
print(my_list2)
