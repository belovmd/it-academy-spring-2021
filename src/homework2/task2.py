"""Homework2 - task2

Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
•    my_string.split([chars]) возвращает список строк.
•    len(list) - количество элементов в списке

"""

import string

in_str = '"Python" is an interpreted, high-level and general-purpose programmmmmming language!'

words = in_str.split()
max_len = 0
result = set()
for word in words:
    word = word.strip(string.punctuation)
    if len(word) > max_len:
        max_len, result = len(word), set((word, ))
    elif len(word) == max_len:
        result.add(word)

if len(result):
    print('MAX length %s chars have words: %s' % (max_len, ', '.join(result)))
