"""
Task 2.

Создайте декоратор,
который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""

import json


def my_dec(func):

    def wrapper(*args, **kwargs):

        value = func(*args, **kwargs)

        try:
            with open('./results.json', 'r') as file:
                results = json.load(file)
        except IOError:
            results = {}
        finally:
            if func.__name__ not in results:
                results[func.__name__] = []
            results[func.__name__].append(value)
            with open('results.json', 'w') as file:
                json.dump(results, file, indent='    ')

        return value

    return wrapper


def add_two(num_):
    return num_ + 2


add_two = my_dec(add_two)


@my_dec
def add_three(num_):
    return num_ + 3


add_two(2)
add_two(3)
add_two(4)
add_three(4)
add_three(5)
add_three(6)
add_three(7)
