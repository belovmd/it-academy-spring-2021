"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.

Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

my_string = input("Введите предложение: ").split()
new_string = ''.join(my_string)
output_list = []
for symbol in new_string:
    if symbol not in output_list:
        output_list.append(symbol)
output_string = ''.join(output_list)
print(output_string)
