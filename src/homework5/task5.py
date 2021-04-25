"""
Написать программу
которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def nearest_2pow(n):
    k = 1
    while k < n:
        k <<= 1
    return k if (abs(n - k) <= abs(n - (k >> 1))) else k >> 1


print(nearest_2pow(8))
print(nearest_2pow(20))
print(nearest_2pow(1))
print(nearest_2pow(13))
