# Создайте декоратор, который вызывает задекорированную функцию пока она
# не выполнится без исключений (но не более n раз - параметр декоратора).
# Если превышено количество попыток, должно быть возбуждено исключение
# типа TooManyErrors

class TooManyErrors(RuntimeError):
    pass


def dec_parametrized(num):
    def dec(func):
        counter = 0

        def wrapper():
            nonlocal counter
            try:
                while True:
                    try:
                        result = func()
                    except (ZeroDivisionError, ValueError):
                        counter += 1
                    else:
                        break
                    if counter >= num:
                        counter = 0
                        raise TooManyErrors('Превышено количество попыток')
            except RuntimeError as error:
                print(error)
            else:
                return result
        return wrapper
    return dec


@dec_parametrized(3)
def my_super_func():
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите вторе число: '))
    res = number_1 / number_2
    return print(res)


my_super_func()
