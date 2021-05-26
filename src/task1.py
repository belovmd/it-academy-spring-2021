"""
Homework 5 - Task1
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


from inspect import getmembers
from inspect import isfunction
import task1_functions as t_func

functions = {func[0]: func[1] for func in getmembers(t_func, isfunction)}


def runner(*args):
    if not args:
        for func in functions.values():
            print(func())
    else:
        for func in args:
            print(functions[func]())


runner()
runner('func1')
runner('func4', 'func3')
