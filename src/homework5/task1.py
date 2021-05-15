"""Оформите решение задач из прошлых домашних работ в функции.

Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import functions_for_task1 as funcs_import


def runner(*args):
    def call_fun(fun):
        """Функция call_fun(fun)

        вызывает непосредственно требуемую функцию из модуля
        """

        return getattr(funcs_import, fun)()

    if not len(args):
        functions = [fun for fun in dir(funcs_import)
                     if not fun.startswith('__') and '__call__' in dir(fun)]
        # вызываем фунции через print для наглядонсти
        print(*[call_fun(fun) for fun in functions], sep='\n')
    else:
        print(*[call_fun(fun) for fun in args], sep='\n')


runner()
runner('hmw2_tsk2')
runner('hmw2_tsk3')
runner('hmw2_tsk3', 'hmw2_tsk2')
