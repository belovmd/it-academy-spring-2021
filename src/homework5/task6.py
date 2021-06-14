# Вводится число найти его максимальный делитель, являющийся степенью двойки.

def maximum_divisor(num):

    power_of_two = int(num ** 0.5 // 1)
    for power in range(power_of_two, 0, -1):
        if not num % (2 ** power):
            print(2 ** power)
            break


maximum_divisor(10)
maximum_divisor(16)
maximum_divisor(12)
