# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

string = 'abc cde def'
newstring = ''
for char in string.replace(' ', ''):
    if char not in newstring:
        newstring += char
print(newstring)
