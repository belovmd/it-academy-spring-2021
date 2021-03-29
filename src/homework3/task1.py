"""Homework 3 - Task 1"""


def fizz_buzz(start: int = 1, stop: int = 101) -> None:
    """FizzBuzz

    Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
    вместо чисел кратный 5 пишет Buzz,  а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.
    """
    for number in range(start, stop):
        output_value = ''
        if not number % 3:
            output_value = 'Fizz'
        if not number % 5:
            output_value += 'Buzz'
        if not output_value:
            output_value = number
        print(output_value, end='')


if __name__ == '__main__':
    fizz_buzz()
