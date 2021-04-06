"""Homework 4 - Task 7"""


def greatest_common_divisor(num1: int, num2: int) -> int:
    """Оглянемся назад. Числа

    Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
    алгоритма Евклида (мы не знаем функции и рекурсию).
    """
    while num1 != num2:
        num1, num2 = min(num1, num2), abs(num1 - num2)
    return num1


if __name__ == '__main__':

    print(greatest_common_divisor(18, 30))
