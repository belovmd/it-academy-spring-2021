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
        """
        Функция call_fun вызывает непосредственно требуемую функцию из модуля
        """
        return getattr(funcs_import, fun)()

    if not len(args):  # если функция runner() вызвана без аргументов
        # извлекаем функции модуля
        functions = [fun for fun in dir(funcs_import)
                     if not fun.startswith('__')]
        # вызываем фунции через print для наглядонсти
        print(*[call_fun(fun) for fun in functions], sep='\n')
        # иначе вызов функции реализуется через for-loop
        # for fun in functions:
        #     call_fun(fun)
    else:
        # args - это tuple, поэтому посчитаем его длинну для вызова функции
        functions = args
        if len(functions) == 1:
            print(call_fun(functions[0]))
            #  call_fun(functions[0])
        else:
            print(*[call_fun(fun) for fun in functions], sep='\n')
            # for fun in functions:
            #     call_fun(fun)


runner()
runner('hmw2_tsk2')
runner('hmw2_tsk3')
runner('hmw2_tsk3', 'hmw2_tsk2')
