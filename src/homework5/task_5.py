"""
Task 5.

Написать программу,
которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
Задачу поместите в файл task5.py в папке src/homework5.
"""


def find_pow(num_):
    pow_ = 1
    while pow_ < num_:
        pow_ = pow_ << 1

    if pow_ - num_ < num_ - (pow_ >> 1):
        return pow_
    else:
        return pow_ >> 1


print(find_pow(10))
print(find_pow(20))
print(find_pow(1))
print(find_pow(13))
