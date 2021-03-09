""""
Homework 2 (task 2)

Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Использовалось 2 функции replace с целью убрать как точки так и запятые
Перебрать слова в предложении и если длина нового слова больше предыдущего, то записываем его в переменную.
В итоге остается самое длинное слово
"""

text = str(input('Введите строку: ').replace(' ', ''))

rus_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
count_lower = 0
count_upper = 0

for symbol in text:

    if symbol.islower() and rus_letters.find(str(symbol)) == -1:
        count_lower += 1

    elif symbol.isupper() and rus_letters.find(str(symbol).lower()) == -1:
        count_upper += 1

print(f" Нижний регистр - {count_lower} символов. Верхний регистр {count_upper} символов")
