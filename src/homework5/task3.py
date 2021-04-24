"""Homework 5 - Task 3

Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых
чисел, отсортированных по возрастанию, которая этот список “сворачивает”.

get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  #  "0-4, 7-8, 10"
get_ranges([4,7,10])  # "4, 7, 10"
get_ranges([2, 3, 8, 9])  # "2-3, 8-9"
"""


def get_ranges(lst: list) -> list:

    def str_to_append(start, stop):
        return str(start) if start == stop else str(start) + '-' + str(stop)

    result = []
    start = stop = None
    for element in lst:
        if start is None:
            start = stop = element
            continue
        if element == stop + 1:
            stop = element
            continue
        result.append(str_to_append(start, stop))
        start = stop = element
    result.append(str_to_append(start, stop))
    return result


if __name__ == '__main__':
    print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
    print(get_ranges([4, 7, 10]))
    print(get_ranges([2, 3, 8, 9]))
    print(get_ranges([2]))
