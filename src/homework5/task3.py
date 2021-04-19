"""
Сворачивание списка

Реализовать функцию get_ranges
которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(input_list):
    result = ''
    parts = []
    start_part = 0

    for i in range(0, len(input_list) - 1):
        if input_list[i] != input_list[i + 1] - 1:
            parts.append(input_list[start_part:i + 1])
            start_part = i + 1
    parts.append(input_list[start_part:])

    for part in parts:
        if len(part) == 1:
            result += '{},'.format(part[0])
        else:
            result += '{}-{},'.format(part[0], part[-1])

    return result[:-1]


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
