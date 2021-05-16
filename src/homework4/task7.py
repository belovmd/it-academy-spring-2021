# Task 7  Оглянемся назад. Числа.
# Даны два натуральных числа. Вычислите их наибольший общий делитель при
# помощи алгоритма Евклида (мы не знаем функции и рекурсию).

a, b = 12, 198

if a > b:
    num1, num2 = a, b
else:
    num1, num2 = b, a

nod = True

while nod and num1 and num2:
    nod = num1 % num2
    num1, num2 = num2, nod
    if not nod:
        print("НОД равен", num1)
        break
else:
    print("Ошибка. Одно из чисел равно 0")
