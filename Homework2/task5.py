# 5. Выведите n-ое число Фибоначчи, используя только временные переменные
i, n1, n2 = 0, 0, 1

number_fibonachi = int(input('Введите номер элемента числа фибоначи:'))
while i < number_fibonachi - 2:
    sum = n1 + n2
    n1 = n2
    n2 = sum
    i = i + 1

print(n2)
