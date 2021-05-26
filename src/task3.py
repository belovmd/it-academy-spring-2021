"""
Homework 5 - Task3
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая
этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst_):
    str_ = ""
    length = 1
    for i in range(1, len(lst_) + 1):
        if i == len(lst_) or lst_[i] - lst_[i - 1] != 1:
            if length == 1:
                str_ += "{},".format(lst_[i - length])
            else:
                str_ += "{}-{},".format(lst_[i - length], lst_[i - 1])
                length = 1
        else:
            length += 1
    return str_.strip(",")


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
