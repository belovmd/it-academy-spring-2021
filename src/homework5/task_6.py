"""
Task 6.

Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def find_div(num_):
    pow_ = 1

    while pow_ <= num_:
        pow_ = pow_ << 1
    pow_ = pow_ >> 1

    while num_ % pow_:
        pow_ = pow_ >> 1

    return pow_


print(find_div(10))
print(find_div(16))
print(find_div(12))
