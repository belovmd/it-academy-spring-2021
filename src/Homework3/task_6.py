# Task 6. Дан список целых чисел. Требуется переместить все ненулевые элементы
# в левую часть списка, не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.

numbers = [0, 1, 2, 3, 8, 9, 10, 0, 5, 4, 0, 3, 0]

for element in numbers:
    numbers.remove(0)
    numbers.append(0)

print(numbers)
