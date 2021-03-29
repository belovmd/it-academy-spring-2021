# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы
str = input()
new_str = []

for i in str:
    if i not in new_str and i != ' ':
        print(i, end='')
        new_str.append(i)
