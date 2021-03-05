"""Homework2 - task5

Выведите n-ое число Фибоначчи, используя только временные переменные, циклические
операторы и условные операторы. n - вводится

"""


n = 15
if not isinstance(n, int) or n <= 0:
    print('Not valid input number (int from 1 to ... is expected)')
    raise ValueError


for i in range(n):
    if i > 1:
        cur, prev = cur + prev, cur
    elif i == 0:
        cur = 0
    elif i == 1:
        cur, prev = 1, 0

    if i == n-1:
        print('%s fibonacci number is: %s' % (n, cur))
