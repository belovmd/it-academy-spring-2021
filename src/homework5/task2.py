"""Homework 5 - Task 2

Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов, не только
текущий запуск программы)
"""
from datetime import datetime


def file_logging_dec(log_file_name):

    def logging_dec(func):
        logger_format = '{time} - {name}({args},{kwargs}): {message}\n'
        logger_name = __name__ + '.' + func.__name__

        def wrapper(*args, **kwargs):
            with open(log_file_name, 'a') as logger:
                message = ''
                try:
                    result = func(*args, **kwargs)
                    message = str(result)
                    return result
                except Exception as ex:
                    message = 'ERROR - ' + str(ex)
                finally:
                    logger.write(logger_format.format(
                        time=str(datetime.now()),
                        name=logger_name,
                        message=message,
                        args=','.join([str(arg) for arg in args]),
                        kwargs=','.join([str(key) + '=' + str(val) for key, val in kwargs.items()])
                    ))
        return wrapper
    return logging_dec


if __name__ == '__main__':

    @file_logging_dec('funcsLog.txt')
    def add(a, b):
        return a + b

    @file_logging_dec('funcsLog.txt')
    def sub(a, b):
        return a - b

    @file_logging_dec('funcsLog.txt')
    def mult(a, b):
        return a * b

    @file_logging_dec('funcsLog.txt')
    def div(a, b):
        return a / b

    add(5, 3)
    sub(5, 3)
    mult(5, 3)
    div(5, 0)
