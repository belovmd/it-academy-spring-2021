'''
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''


import example_module_for_task1


def runner(*args):
    func_lst = []
    if not args:
        func_lst = [elem for elem in dir(example_module_for_task1)
                    if elem[:2] != "__" and elem[:1] != "_"
                    and callable(getattr(example_module_for_task1, elem))]
    elif len(args) == 1:
        func_lst.append(args[0])
    elif len(args) > 1:
        func_lst = list(args)
    for func in func_lst:
        getattr(example_module_for_task1, func)()

print("Вызов всех функций:")
runner()
print("\nВызов одной функции:")
runner("print_hello")
print("\nВызов несrольких функий:")
runner("print_hello", "print_world")
