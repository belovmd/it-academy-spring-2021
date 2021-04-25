"""
Вводится число найти
его максимальный делитель,
являющийся степенью двойки.
10(2) 16(16), 12(4).
"""


def max_pow2(n):
    pow2 = 1
    result = 1
    while pow2 <= n:
        if not n % pow2:
            result = pow2
        pow2 = pow2 << 1
    return result


print(max_pow2(10))
print(max_pow2(16))
print(max_pow2(12))


