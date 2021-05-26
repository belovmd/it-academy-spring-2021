"""
Homework 5 - Task2
Создайте декоратор, который хранит результаты вызовов
функции (за все время вызовов, не только текущий запуск программы)
"""


from datetime import datetime


def my_dec(func):
    def wrapper(*args, **kwargs):
        var_between_runs = []

        with open('task2_result.txt', 'r') as fh:
            for line in fh:
                var_between_runs.append(line.strip())

        result = func(*args, **kwargs)
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        str_ = "{} {} {}".format(dt, str(func.__name__), str(result))
        var_between_runs.append(str_)

        with open('task2_result.txt', 'w') as fh2:
            for line1 in var_between_runs:
                fh2.write(str(line1) + "\n")
            fh2.close()
        return result
    return wrapper


@my_dec
def func1(a, b):
    return a + b


@my_dec
def func2(a, b):
    return a * b


@my_dec
def func3(a, b):
    return a - b


func2(6, 74)
func1(3, 915)
func3(44, 21)
