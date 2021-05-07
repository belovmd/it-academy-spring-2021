# Task 5. Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке только
# один раз. Элементы нужно выводить в том порядке, в котором они встречаются
# в списке.

original = input("Введите элементы: ").split()
result = []

[result.append(element) for element in original if element not in result]

[print(symbol) for symbol in result]
