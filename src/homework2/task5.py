"""Выведите n-ое число Фибоначчи,

используя только временные переменные, циклические операторы и условные операторы. n - вводится
"""


def number_fib(n):
    num_fib = n + 1
    num1, num2 = 0, 1

    while n > 0:
        num1, num2 = num2, num1 + num2
        n -= 1

    print(num_fib, "число Фибоначчи:", num1)


# Testing
for num in range(10):
    number_fib(num)
