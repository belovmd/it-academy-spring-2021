# Даны два натуральных числа. Вычислите их наибольший общий делитель
# при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

num_a = 18
num_b = 30
while num_a and num_b:
    if num_a > num_b:
        num_a = num_a % num_b
    else:
        num_b = num_b % num_a
else:
    print(num_a + num_b)
