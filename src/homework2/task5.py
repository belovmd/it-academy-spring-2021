"""Homework2 - task5

Выведите n-ое число Фибоначчи, используя только
временные переменные, циклические операторы и
условные операторы. n - вводится
"""

fib_number = int(input("Input number of Fibonacci: "))
first_fib = 0
second_fib = 1

for number in range(1, fib_number):
    first_fib, second_fib = second_fib, first_fib + second_fib
print(first_fib)
