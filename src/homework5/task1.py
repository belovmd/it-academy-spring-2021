# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции

import task1_func
from inspect import isfunction


def runner(*args):

    list_of_attr = dir(task1_func)
    for func in list_of_attr:
        attr = getattr(task1_func, func)
        if not args:
            if isfunction(attr):
                attr()
        else:
            if isfunction(attr) and func in args:
                attr()


runner()
runner('task2')
runner('task1', 'task3', 'task7')
