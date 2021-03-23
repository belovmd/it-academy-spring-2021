"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
"""

str_ = str(input('Введите строку:'))
unique_str_without_space = ''

for letter in str_:
    if letter not in unique_str_without_space and letter != ' ':
        unique_str_without_space += letter
print('Строка без пробелов и дубликатов', unique_str_without_space)
