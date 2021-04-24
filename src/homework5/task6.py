"""Homework 5 - Task 6

Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_divisor_that_is_power_of_two(number):
    power_of_two = 1
    max_divisor = 1
    while power_of_two <= number:
        if not number % power_of_two:
            max_divisor = power_of_two
        power_of_two <<= 1
    return max_divisor


if __name__ == '__main__':
    print('Max divisor that is a power of two for the number {} is {}'.format(
        10, max_divisor_that_is_power_of_two(10)
    ))
    print('Max divisor that is a power of two for the number {} is {}'.format(
        16, max_divisor_that_is_power_of_two(16)
    ))
    print('Max divisor that is a power of two for the number {} is {}'.format(
        12, max_divisor_that_is_power_of_two(12)
    ))
