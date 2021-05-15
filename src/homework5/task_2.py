"""
Task 2.

Создайте декоратор,
который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""


def my_dec(func):
    results = []

    def wrapper(*args, **kwargs):

        nonlocal results
        if args[0] == 'check':
            print(f"Result of all calls of {func.__name__}: {results}")
            return

        value = func(*args, **kwargs)

        results.append(value)

        return value

    return wrapper


def func_1(num_):
    return num_ + 2


func_1 = my_dec(func_1)

func_1(2)
func_1(3)
func_1(4)
func_1('check')


@my_dec
def func_2(num_):
    return num_ + 3


func_2(4)
func_2(5)
func_2(6)
func_2('check')
