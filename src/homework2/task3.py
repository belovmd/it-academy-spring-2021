"""Homework2 - task3

Вводится строка. Требуется удалить из нее повторяющиеся
символы и все пробелы. Например, если было введено
"abc cde def", то должно быть выведено "abcdef".
"""

input_string = "abc cde def def abc"
new_string = ""

for symbol in input_string:
    if symbol != " ":
        if symbol not in new_string:
            new_string += symbol
print(new_string)
