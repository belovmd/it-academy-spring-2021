# Выведите n-ое число Фибоначчи, используя только временные переменные
n = int(input('Введите номер элемента числа фибоначи:'))
i = 0
n1 = 0
n2 = 1

while i < n - 2:
    sum = n1 + n2
    n1 = n2
    n2 = sum
    i = i + 1

print(n2)
