# Task 3 — Реализовать функцию get_ranges которая получает на вход непустой
# список неповторяющихся целых чисел, отсортированных по возрастанию,
# которая этот список “сворачивает”.
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def cleaning(lst):
    for str_ in lst:
        if isinstance(str_, str) is True:
            n = str_.find("-")
            if str_[:n] == str_[n + 1:]:
                lst.insert(lst.index(str_), str_[:n])
                lst.remove(str_)
    return lst


def list_changes(lst):
    new_lst, n1, n2, change = [], 0, 1, 1
    while len(lst) >= 3:
        if lst[n1] + change == lst[n2]:
            n2 += 1
            change += 1
        else:
            new_lst.append("{}-{}".format(lst[n1], lst[n2 - 1]))
            lst = lst[n2:]
            n1, n2, change = 0, 1, 1
    if len(lst) == 2:
        if lst[0] + 1 == lst[1]:
            new_lst.append("{}-{}".format(lst[0], lst[1]))
        else:
            new_lst.append(str(lst[0]))
            new_lst.append(str(lst[1]))
    else:
        new_lst.append(str(lst[0]))
    return new_lst


print(cleaning(list_changes([0, 1, 2, 3, 4, 7, 8, 10])))
print(cleaning(list_changes([4, 7, 10])))
print(cleaning(list_changes([2, 3, 8, 9])))
