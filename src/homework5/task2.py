# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

def function_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, *kwargs)
        with open("function_result.txt", "a") as fh:
            fh.write(result + "\n")
        return result

    return wrapper


@function_result
def i():
    return "I don't"


@function_result
def understand():
    return "understand"


@function_result
def anything():
    return "anything"


i()
understand()
anything()
