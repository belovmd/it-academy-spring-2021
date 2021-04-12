# Даны два натуральных числа. Вычислите их наибольший общий делитель при
# помощи алгоритма Евклида (мы не знаем функции и рекурсию).
number_1 = int(input())
number_2 = int(input())

while number_1 and number_2:
    if number_1 > number_2:
        number_1 %= number_2
    else:
        number_2 %= number_1

print('Наибольший общий делитель: ', max(number_1, number_2))
