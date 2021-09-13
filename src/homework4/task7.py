# Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
# алгоритма Евклида (мы не знаем функции и рекурсию).

first_num = int(input('Введите число №1 '))
second_num = int(input('Введите число №2 '))

if first_num < second_num:
    first_num, second_num = second_num, first_num
elif first_num == second_num:
    print("НОД = ", first_num)

while first_num > second_num:
    first_num = first_num % second_num
    if first_num:
        first_num, second_num = second_num, first_num
    else:
        print("НОД = ", first_num + second_num)
