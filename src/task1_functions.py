"""
Homework 5 - Task1(Functions)
Оформите решение задач из прошлых домашних работ в функции.
"""


def func1(number=21):
    dict_1 = {x: x ** 3 for x in range(1, number)}
    return dict_1


def func2():
    lst_1 = [1, 2, 3, 4]
    lst_2 = [3, 4, 5, 6]
    result = (set(lst_1) & set(lst_2))
    return len(result)


def func3(str_=" some text   here hello    "):
    return len(str_.split())


def func4():
    lst_ = ["a", "b", "c"]
    tpl_ = tuple(lst_)
    return tpl_, type(tpl_)
