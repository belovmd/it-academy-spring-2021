'''
Написать программу которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
'''


def get_power_of_two(num):
    len_num = len(bin(num)) - 3      # -3 потому что первых два символа 0b и нужно еще скинуть оди разряд
    less_p_two = 0b1 << len_num      # 1000 = 0b1 << 3
    greate_p_two = 0b1 << (len_num + 1)
    if num - less_p_two > greate_p_two - num:
        return greate_p_two
    else:
        return less_p_two


print("{}({})".format(20, get_power_of_two(20)))
print("{}({})".format(10, get_power_of_two(10)))
print("{}({})".format(13, get_power_of_two(13)))
print("{}({})".format(1, get_power_of_two(1)))
