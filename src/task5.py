"""Написать программу которая находит ближайшую степень двойки.

10(8), 20(16), 1(1), 13(16)
"""
import math


def power_of_two(num):
    return '{}({})'.format(num, 2**round(math.log2(num)))


print(power_of_two(10))
print(power_of_two(20))
print(power_of_two(1))
print(power_of_two(13))
