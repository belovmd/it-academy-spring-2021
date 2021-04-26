'''Вводится число найти его максимальный
делитель, являющийся степенью двойки.
10(2) 16(16), 12(4).'''

MASK_BIN = 0b111111111111111111111111   # Тут использую маску, потому что инверсия
LEN_MASK_BIN = len(bin(MASK_BIN)) - 2   # работает ~a = -(a + 1), а не как обычная инверсия битов


def get_mask(num):
    len_num = len(bin(num)) - 2
    power_of_two = \
        MASK_BIN >> (LEN_MASK_BIN - len_num)
    return power_of_two


def get_power_of_two(num):
    current = num
    mask = get_mask(num)
    while num & mask:
        current = num & mask
        mask = mask >> 1
    return current


print("{}({})".format(10, get_power_of_two(10)))
print("{}({})".format(12, get_power_of_two(12)))
print("{}({})".format(16, get_power_of_two(16)))
print("{}({})".format(24, get_power_of_two(24)))
print("{}({})".format(32, get_power_of_two(32)))
