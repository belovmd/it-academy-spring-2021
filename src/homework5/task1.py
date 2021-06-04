# Task 1 — Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и
# setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции.

import my_funcs
from my_funcs import blocks
from my_funcs import histogram
from my_funcs import stars

funcs = (histogram(), stars(), blocks())


def runner(*args):
    for func in funcs:
        attr = getattr(my_funcs, func)
        if not args:
            return attr
        else:
            return funcs


runner()
runner("stars")
runner("stars", "blocks")
