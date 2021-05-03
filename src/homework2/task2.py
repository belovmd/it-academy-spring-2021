"""
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""

import string

sentence = str(input('Введите предложение со знаками препинания:'))

# Удаление знаков препинания в строке
for symbol in string.punctuation:
    sentence = sentence.replace(symbol, ' ')

# Поиск самого длинного слова
words = sentence.split(' ')
longest_word = ''

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print('Самое длинное слово', longest_word)
