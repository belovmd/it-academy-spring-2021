'''
3. Реализовать функцию get_ranges которая получает на вход непустой
список неповторяющихся целых чисел, отсортированных по
возрастанию, которая этот список “сворачивает”
'''


def get_ranges(lst_):
    lst_sec = insert_comma_between(wrapper_list(lst_))
    return ''.join(str(elem) for elem in lst_sec)


def wrapper_list(lst_):
    pos = 0
    wrap_list = list()
    previous_elem = lst_.pop(0)
    wrap_list.append(previous_elem)
    state = False
    while pos < len(lst_):
        if lst_[pos] - previous_elem == 1 and pos != len(lst_) - 1:
            state = True
            previous_elem = lst_[pos]
            pos += 1
            continue
        elif state and pos == len(lst_) - 1:
            wrap_list.append('-')
            wrap_list.append(lst_[pos])
            break
        elif state:
            wrap_list.append('-')
            wrap_list.append(previous_elem)
            state = False
        previous_elem = lst_[pos]
        wrap_list.append(lst_[pos])
        pos += 1
    return wrap_list


def insert_comma_between(lst_):
    new_lst = list()
    for pos in range(len(lst_)):
        if pos != len(lst_) - 1 and isinstance(
                lst_[pos], int) and \
                isinstance(lst_[pos + 1], int):
            new_lst.append(lst_[pos])
            new_lst.append(',')
            continue
        new_lst.append(lst_[pos])
    return new_lst


lst_example = [1, 2, 3, 4, 10, 11, 20, 23, 36, 37, 38]
print(get_ranges(lst_example))
