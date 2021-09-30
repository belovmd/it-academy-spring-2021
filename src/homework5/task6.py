# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).

def num(number):
    degree = -1
    lst_of_divisor = []
    while True:
        degree += 1
        if 2 ** degree <= number and number % (2 ** degree) == 0:
            lst_of_divisor.append(2**degree)
            continue
        return lst_of_divisor[-1]


print(num(16))
