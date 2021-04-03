# Task 1 — FizzBuzz
# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
# кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
# одновременно кратных и 3 и 5 - FizzBuzz

result = []

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        result.append("FizzBuzz")
    elif num % 3 == 0:
        result.append("Fizz")
    elif num % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(num))

print(", ".join(result))
