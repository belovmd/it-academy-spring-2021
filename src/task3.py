# Даны два списка чисел. Посчитайте, сколько различных чисел содержится
# одновременно как в первом списке, так и во втором.

first = [1, 2, 3, 4]
second = [3, 4, 5, 6, 7]
set_from_first = set(first)
set_from_second = set(second)
set_result = set_from_first & set_from_second
print(len(set_result))
