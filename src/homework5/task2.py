# Task 2 — Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

# Sorry but I don't know the other way to store data between restarts of the
# program. Probably it implied using of closure or something but I don't
# understand how to do it without losing the counter after the end of program.


def counter(func):
    def wrap(*args):
        with open("storage.txt", "r") as file:
            text = file.read()
        rewriting = open("storage.txt", "w")
        if not text:
            rewriting.write("1")
        else:
            rewriting.write(str(int(text) + 1))
        rewriting.close()
        return func(*args)

    with open("storage.txt", "r") as file_:
        result = file_.read()
    print(result)
    return wrap


@counter
def f(num):
    return num

print(f(1))
print(f(2))
print(f(3))

counter(f)