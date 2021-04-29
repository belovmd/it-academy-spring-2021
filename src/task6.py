"""Вводится число найти его максимальный делитель,

являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_divisor(num):
    if num % 2:
        return 'Число не делится на 2'
    else:
        count = 0
        div = num
        while not div % 2:
            div /= 2
            count += 1
        return '{}({})'.format(num, 2 ** count)


print(max_divisor(10))
print(max_divisor(16))
print(max_divisor(12))
