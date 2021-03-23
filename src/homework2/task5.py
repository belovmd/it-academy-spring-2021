"""
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. Числа Фибоначчи – это ряд чисел,
в котором каждое следующее число равно сумме двух предыдущих.
"""

fibonacci_num_1 = 1
fibonacci_num_2 = 1

fibonacci_n = int(input('Введите n (номер элемента ряда Фибоначчи):'))

i = 2
while i < fibonacci_n:
    fibonacci_sum = fibonacci_num_1 + fibonacci_num_2
    fibonacci_num_1 = fibonacci_num_2
    fibonacci_num_2 = fibonacci_sum
    i = i + 1
print(fibonacci_num_2)
