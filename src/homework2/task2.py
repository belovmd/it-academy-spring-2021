"""Homework2 - task2

Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
•    my_string.split([chars]) возвращает список строк.
•    len(list) - количество элементов в списке

"""


in_str = '"Python" is an interpreted, high-level and general-purpose programmmmming language!'
# punctuation = string.punctuation
punctuation = '.,!?"#()[];:<>'

words = in_str.translate(str.maketrans('', '', punctuation)).split()

res = ['']
for word in words:
    print(word, len(word), len(res[0]))
    if len(word) > len(res[0]):
        res = [].append(word)
    elif len(word) == len(res[0]):
        res.append(word)

if len(res):
    print('MAX length %s chars have words: %s' % (len(res[0]), ', '.join(res)))
