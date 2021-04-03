# Task 5. Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке только
# один раз. Элементы нужно выводить в том порядке, в котором они встречаются
# в списке.

orig_numbers = [int(num) for num in input("Введите числа: ").split()]
result = []

[result.append(number) for number in orig_numbers if number not in result]

print(result)
