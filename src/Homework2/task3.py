""""
Homework2 (task 3)

Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".


"""
RESULT = ''
main_str = (input('Введите предложение: '))
str_without_spaces = main_str.replace(' ', '')
while str_without_spaces:
    RESULT = RESULT + str_without_spaces[0]
    str_without_spaces = str_without_spaces.replace(str_without_spaces[0], '')
print(RESULT)
