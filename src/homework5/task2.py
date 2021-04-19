"""
Декоратор хранящий результаты вызова функции

Создайте декоратор,
который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""

FILE_NAME = 'log_file_for_task_2.txt'


def log_calls(func):
    try:
        with open(FILE_NAME, 'r') as file_log:
            list_log = file_log.readlines()
    except FileNotFoundError:
        list_log = []
        with open(FILE_NAME, 'tw'):
            pass

    def wrapper(*args, **kwargs):
        nonlocal list_log
        result = func(*args, **kwargs)
        list_log.append(str(result))
        with open(FILE_NAME, 'a') as file_write:
            file_write.write(str(result) + '\n')
        return result
    return wrapper


@log_calls
def my_func(n):
    return n ** n


print(my_func(my_func(3)))
