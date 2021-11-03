# 1. FizzBuzz
# Напишите программу, которая печатает цифры от 1 до 100,
# # но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz

from random import randrange

x = randrange(0, 101)  # [0; a)

print("Our generated number - ", x, ".")
if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print("You should try once again.")
