'''2. Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)'''

from datetime import  datetime
import os.path


FILE_NAME = "log_" + datetime.strftime(
    datetime.now(), "%Y.%m.%d_%H:%M:%S") \
            + ".txt"


def create_log(func):                                  # Не уверен что правильно понял задание.
    path = "./task2_log/{}".format(FILE_NAME)          # При каждом запуске программы я в папке task2_log

    def wrapper(*args, **kwargs):                      # создавал файл имя которого приставка log_
        if os.path.exists(r"{}".format(path)):         # и datetime запуска программы. Туда писал время запуска функции,
            file_ = open(path, "a")                    # имя и результат
        else:
            file_ = open(path, "w")
        result = func(*args, **kwargs)
        current_time = datetime.strftime(
            datetime.now(), "%Y.%m.%d %H:%M:%S")
        func_name = func.__name__
        file_.write("{} {} => {}\n".format(
            current_time, func_name, result))
        file_.close()
        return result
    return wrapper


@create_log
def sum(a, b):
    return a + b


@create_log
def mult(a, b):
    return a * b


sum(1, 2)
mult(1, 2)
sum(3, 4)
