"""
Вводится строка.

Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

my_str = input('Введите строку: ')
new_str = ''

for i in my_str:
    if i not in new_str and i != ' ':
        new_str += i

print(new_str)
