""""
Homework2 (task_2)
Посчитать количесвто символов самого длинного слова в предложении исключая знаки препинания

"""
from string import punctuation

base_string = (input("Введите строку: "))
MAX_STRING = ""
cleaning = str.maketrans('', '', punctuation)
words = base_string.translate(cleaning).split()
for _x in words:
    if len(_x) > len(MAX_STRING):
        MAX_STRING = _x

print(MAX_STRING)
