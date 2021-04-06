"""Homework 4 - Task 1"""


def cubes_dict(start: int, stop: int) -> dict:
    """Dict comprehensions

    Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20,
    а значениями кубы этих чисел.
    """
    return {key: key ** 3 for key in range(start, stop)}


if __name__ == '__main__':
    print(cubes_dict(1, 21))
