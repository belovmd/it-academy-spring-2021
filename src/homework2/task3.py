"""Homework2 - task3

Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".

"""


in_str = 'abc cde def'
res = []
for c in in_str:
    if (c in res) or (c == ' '):
        continue
    res.append(c)

res = ''.join(res)
print('Result:', res)
