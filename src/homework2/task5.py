# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится
first_number = second_number = 1
num = int(input())

for el in range(3, num + 1):
    first_number, second_number = second_number, first_number + second_number
    fib_number = second_number
print(fib_number)
