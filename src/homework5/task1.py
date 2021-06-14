# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner.
# 1. runner() – все фукнции вызываются по очереди.
# 2. runner(‘func_name’) – вызывается только функцию func_name.
# 3. runner(‘func’, ‘func1’...) - вызывает все переданные функции.


from inspect import isfunction
import homework2_func


def runner(*args):

    list_of_attr = dir(homework2_func)
    for func in list_of_attr:
        attr = getattr(homework2_func, func)
        if not args:
            if isfunction(attr):
                attr()
        else:
            if isfunction(attr) and func in args:
                attr()


runner()
runner('fibonacci_number')
runner('triangle', 'palindrome', 'fibonacci_number')
