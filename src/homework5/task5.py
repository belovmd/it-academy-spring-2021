# Написать программу, которая находит ближайшую степень двойки
# к введенному числу.


def nearest_power_of_two(num):
    power_of_two = int(num ** 0.5 // 1)
    before_num = 2 ** power_of_two
    after_num = 2 ** (power_of_two + 1)
    if num == 1:
        print(1)
    elif after_num - num < num - before_num:
        print(after_num)
    else:
        print(before_num)


nearest_power_of_two(10)
nearest_power_of_two(20)
nearest_power_of_two(11)
nearest_power_of_two(13)
