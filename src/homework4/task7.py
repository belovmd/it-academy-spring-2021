# Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
# алгоритма Евклида (мы не знаем функции и рекурсию).

first_num = 12312
second_num = 4236546456

if first_num > second_num:

    while first_num and second_num:

        first_num = first_num % second_num
        second_num = second_num % first_num

else:

    while first_num and second_num:

        second_num = second_num % first_num
        first_num = first_num % second_num

print(first_num, second_num)
