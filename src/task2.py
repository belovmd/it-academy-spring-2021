"""Создайте декоратор,

который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""


def my_dec(func):
    """Функция сохраняет показание счетчика вызовов в файле 'count.txt'"""
    with open('count.txt', 'r') as fh:
        read_count = fh.read()
        if read_count:
            count = int(read_count)
        else:
            count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, count))
        with open('count.txt', 'w') as f:
            f.write(str(count))
        return result
    return wrapper


# Задекорируем для примера простейшую функцию
@my_dec
def hello_print():
    print('Hello, decorator')


hello_print()  # повызываем её
hello_print()
hello_print()
