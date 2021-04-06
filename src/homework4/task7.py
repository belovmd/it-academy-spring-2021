"""Оглянемся назад. Числа

Даны два натуральных числа.
Вычислите их наибольший общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
"""

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if not a % b:
    print("b делится на a, значит НОД:", b)
else:

    divisor = a // b
    remainder = a % b
    lst = []

    while True:
        if a == b * divisor:
            if lst[-2] == 1:
                print("Данные числа являются взаимно простыми, НОД = ", lst[-2])
                break
            else:
                print('Нод = ', lst[-2])
                break
        else:
            # применим алгоритм Евклида для нахождения НОДа
            a = b
            b = remainder
            divisor = a // b
            lst.append(remainder)
            remainder = a % b
            lst.append(remainder)
