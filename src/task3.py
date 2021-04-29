"""Реализовать функцию get_ranges,

 которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // '0-4,7-8,10'
 get_ranges([4,7,10]) // '4,7,10'
 get_ranges([2, 3, 8, 9]) // '2-3,8-9'
 """


def get_ranges(lst):
    ranges = []
    a = b = lst[0]  # a - start of range, b - end of range

    for num in lst[1:] + [None]:
        if num != b + 1:
            ranges.append(str(a) if a == b else "{}{}{}".format(a, "-", b))
            a = num
        b = num
    return ",".join(ranges)


print(get_ranges([4, 7, 10]))
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([2, 3, 8, 9]))
