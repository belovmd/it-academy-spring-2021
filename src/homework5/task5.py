"""Homework 5 - Task 5

Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def closest_power_of_two(number):
    bigger = 1
    while bigger <= number:
        bigger <<= 1
    lower = bigger >> 1
    return bigger if bigger - number <= number - lower else lower


if __name__ == '__main__':
    print('Closest power of two to {} is {}'.format(10, closest_power_of_two(10)))
    print('Closest power of two to {} is {}'.format(20, closest_power_of_two(20)))
    print('Closest power of two to {} is {}'.format(1, closest_power_of_two(1)))
    print('Closest power of two to {} is {}'.format(13, closest_power_of_two(13)))
