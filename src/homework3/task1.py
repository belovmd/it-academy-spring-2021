"""Homework 3 - Task1

Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz
"""

# Find divisible numbers
first_digit = 3
second_digit = 5

for index in range(1, 101):
    answer = ""
    if not index % first_digit:
        answer = "Fizz"
    if not index % second_digit:
        answer += "Buzz"
    if not answer:
        answer = index
    print(answer)
