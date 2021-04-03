# Task 3. Вводится строка. Требуется удалить из нее повторяющиеся
# символы и все пробелы.

original = "abc cde def fge hij kl ml mlk"
new_string = ''

for letter in original.replace(' ', ''):
    if letter not in new_string:
        new_string += letter

print(new_string)
