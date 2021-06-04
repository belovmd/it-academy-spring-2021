# Task 6 — Вводится число найти его максимальный делитель, являющийся степенью
# двойки. 10(2) 16(16), 12(4).

def max_divisor(num):
    base, exponent, current_divisor = 2, 0, 1
    while num >= base ** exponent:
        exponent += 1
        if not num % base ** exponent:
            current_divisor = base ** exponent
    print(current_divisor)


max_divisor(64)
max_divisor(10)
max_divisor(16)
max_divisor(12)
