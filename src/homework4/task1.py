"""
Dict comprehensions

Создайте словарь с помощью генератора словарей,
так чтобы его ключами были числа от 1 до 20,
а значениями кубы этих чисел.
"""


result = {index: index ** 3 for index in range(1, 21)}
print(result)
