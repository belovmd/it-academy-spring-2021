""""
Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz, вместо чисел
кратный 5 пишет Buzz, а вместо чисел одновременно
кратных и 3 и 5 - FizzBuzz
"""

for elem in range(1, 101):
    if not elem % 3 and not elem % 5:
        print("FizzBuzz", end=" ")
    elif not elem % 3:
        print("Fizz", end=" ")
    elif not elem % 5:
        print("Buzz", end=" ")
    else:
        print(elem, end=" ")
