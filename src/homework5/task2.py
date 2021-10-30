# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)
import os.path


def dec(func):

    def wrapper(*args, **kwargs):
        dct = {}
        func_name = func.__name__
        if os.path.exists('text.txt'):
            with open('text.txt', 'r') as fh:
                for line in fh:
                    key, value = line.split()
                    dct[key] = value

        dct[func_name] = str(int(dct.get(func_name, "0")) + 1)
        print(func_name + " количество вызовов: " + dct[func_name])
        with open('text.txt', 'w') as fh:
            for key, value in dct.items():
                fh.write(key + " " + value + "\n")
        result = func(*args, **kwargs)
        return result

    return wrapper


@dec
def func_first():
    print('Первая функция')


@dec
def func_second():
    print('hello world')


func_second()
func_first()
func_second()
