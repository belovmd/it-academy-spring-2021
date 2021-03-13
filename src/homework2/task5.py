# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится
first_number = 1
second_number = 1
num = int(input())

i = 0
while i < num - 2:  # first_number and second_number are known
    fib = first_number + second_number
    first_number = second_number
    second_number = fib
    i = i + 1
print(second_number)
