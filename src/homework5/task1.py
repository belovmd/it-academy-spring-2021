"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

from inspect import isfunction
import tasks_in_functions


def runner(*args):
    list_of_attr = dir(tasks_in_functions)
    for func in list_of_attr:
        attr = getattr(tasks_in_functions, func)
        if not args:
            if isfunction(attr):
                attr()
        else:
            if isfunction(attr) and func in args:
                attr()


runner()
runner("delete_of_punctuation")
runner("delete_of_punctuation", "the_longest_word")
