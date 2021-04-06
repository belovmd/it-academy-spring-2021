"""
Упорядоченный список.

Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""

# Через while-loop

lst1 = [0, 1, 2, 3, 0, 3, 4, 0, 5, 6, 7, 0]
index = len(lst1) - 1
while index >= 0:
    if not lst1[index]:
        lst1.append(lst1.pop(index))
    index -= 1
print(*lst1, sep=" ")

# Через for-loop

lst2 = [0, 1, 2, 3, 0, 3, 4, 0, 5, 6, 7, 0]
counter = 0
for index2 in range(len(lst2)):
    if lst2[index2] != 0:
        print(lst2[index2], end=" ")
    else:
        counter = counter + 1
for element in range(counter):
    print(0, end=" ")
