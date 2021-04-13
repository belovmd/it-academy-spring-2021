# Даны два натуральных числа. Вычислите их наибольший общий делитель
# при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

number1 = 54
number2 = 88

while number1 != 0 and number2 != 0:
    if number1 > number2:
        number1 = number1 % number2
    else:
        number2 = number2 % number1

print(number1 + number2)
