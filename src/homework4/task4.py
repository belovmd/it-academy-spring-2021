# task4

# Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [7, 3, 1, 0, 5, 9]
list_1, list_2 = set(list_1), set(list_2)
amount_of_numbers = len(list_1 ^ list_2)
print('{} различных чисел входит только в один из данных списков.'.format(amount_of_numbers))
