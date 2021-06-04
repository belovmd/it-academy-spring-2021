# Task 1 — Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и
# setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции.

from my_funcs import histogram, stars, blocks

funcs = (my_funcs.histogram(), my_funcs.stars(), my_funcs.blocks())


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
