"""
Task 1.

Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import homework2
import homework3
import homework4

# calls for flake8 proof because of unused imports
homework2.homework2_task1()
homework3.homework3_task1()
homework4.homework4_task1()


def call_all_functions():
    for module in globals().values():
        if "<class 'module'>" in str(type(module)):
            for attr in dir(module):
                if not attr.startswith('_'):
                    method = getattr(module, attr)
                    if callable(method):
                        method()


def find_all_modules():
    modules = []
    for elem in globals().values():
        if "<class 'module'>" in str(type(elem)):
            modules.append(elem)
    return modules


def runner(*args):
    if not args:
        return call_all_functions()

    modules = find_all_modules()

    for func in args:
        for module in modules:
            if not hasattr(module, func):
                continue
            else:
                method = getattr(module, func)
                method()


runner('homework2_task3')
runner('homework2_task3', 'homework3_task5')
runner()
