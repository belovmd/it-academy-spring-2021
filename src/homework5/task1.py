"""Homework 5 - Task 1

Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner. (все станет
проще когда мы изучим модули, getattr и setattr)
runner()  –  все фукнции вызываются по очереди
runner(‘func_name’)  –  вызывается только функцию func_name.
runner(‘func’, ‘func1’...)  -  вызывает все переданные функции
"""


def runner(*names, rerun=True):
    """Функция run

    Осуществляет вызов, доступных в глобальной области видимости вызывающего модуля вызываемых
    объектов по их именам, содержащимся в кортеже names, либо всех, доступных в глобальной области
    видимости вызывающего модуля вызываемых объектов, если кортеж names пуст.

    :param names: упакованные в кортеж позиционные аргументы являющиеся именами переменных,
    ссылающихся на вызываемые объеты, которые необходимо вызвать. Если аргументы не заданы,
    вызываются все вызываемые объекты.
    :param rerun: True, если разрешен повторный вызов объекта, иначе - False
    :return: None
    """
    imported_modules = {}  # key - id объекта модуля, value - объект модуля
    funcs = {}  # key - имя переменной, содержащей ссылку на вызываемый объект,
    # value - кортеж (<имя модуля в котором создана переменная>, <вызываемый объект>)

    for attr, obj in globals().items():
        if attr.startswith('_'):
            continue
        if callable(obj) and obj.__name__ != 'runner':
            funcs.setdefault(attr, []).append((runner.__module__, obj))
        elif type(obj).__name__ == 'module':
            imported_modules.setdefault(id(obj), obj)  # ключ - id (для исключения дублирования)

    for mod_obj in imported_modules.values():
        for attr in dir(mod_obj):
            if not attr.startswith('_') and callable(getattr(mod_obj, attr)):
                funcs.setdefault(attr, []).append((mod_obj.__name__, getattr(mod_obj, attr)))

    processed = {}
    if not names:
        names = funcs.keys()
    for name in names:
        try:
            tuples = funcs[name]
            for mod_name, func_obj in tuples:
                if not rerun and processed.get(id(func_obj)):
                    continue
                print('Calling object "{name}" id{id} from module "{mod}": '.format(
                    name=name,
                    id=id(func_obj),
                    mod=mod_name
                ), end='')
                processed.setdefault(id(func_obj), True)
                res = func_obj()
                print(res)
        except KeyError:
            print('Calling object "{}": ERROR - object is not exist'.format(name))
        except Exception as ex:
            print('ERROR - {}'.format(str(ex)))


if __name__ == '__main__':

    import task5        # импортируется в целях тестирования  # noqa
    # import math         # импортируется в целях тестирования  # noqa
    import functools    # импортируется в целях тестирования  # noqa

    def test1():
        return "I'm test1"

    def test2(x):
        return x

    test3 = test1

    print('---------------- RUNNER with one argument -----------------------')
    runner('test1')
    print('--------------- RUNNER with many arguments ----------------------')
    runner('test1', 'test3', 'blablabla', 'reduce')
    print('--------- RUNNER without arguments (rerun = False) ---------------')
    runner(rerun=False)  # test1 вызывается, test3 не вызывается
    print('--------- RUNNER without arguments (rerun = True) --------------')
    runner()  # test1 вызывается и test3 вызывается
