"""
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""


import datetime
import os.path


def my_dec(func):

    def wrapper(*args, **kwargs):
        dicts = {}
        f_name = func.__name__
        time_now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        if os.path.exists('result_for_task2.txt'):
            with open('result_for_task2.txt', 'r') as fh:
                for line in fh:
                    key, *value = line.split()
                    dicts[key] = " ".join(value)

        dicts[f_name] = str(int(dicts.get(f_name, "0").split()[0]) + 1) + " " + time_now
        print(f_name + " " + dicts[f_name])
        with open('result_for_task2.txt', 'w') as fh:
            for key, value in dicts.items():
                fh.write(key + " " + value + "\n")
        result = func(*args, **kwargs)
        return result

    return wrapper


@my_dec
def function():
    print('it is working')


@my_dec
def function2():
    print('it is working too')


function()
function2()
function2()
