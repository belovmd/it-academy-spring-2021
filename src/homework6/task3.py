# Реализовать функцию get_ranges которая получает на вход непустой список
# неповторяющихся целых чисел, отсортированных по возрастанию,
# которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"

# Аларм!!! Я немного добавил функционала. Функция получает позиционные аргументы в хаотичном
# виде, удаляет повторяющиеся числа и сортирует их

def get_ranges(*args):
    set_ = set(args)
    num_list = list(set_)
    num_list.sort()
    str_ = ""
    len_args = len(num_list)
    for num in range(len_args - 1):
        if (num_list[num] - 1) != num_list[num - 1] and (num_list[num] + 1) == num_list[num + 1]:
            str_ += str(num_list[num]) + '-'
        elif (num_list[num] - 1) == num_list[num - 1] and (num_list[num] + 1) == num_list[num + 1]:
            continue
        else:
            str_ += str(num_list[num]) + ','
    str_ += str(num_list[len_args - 1])
    return print(str_)


get_ranges(3, 46, 7, 8, 0, 2, 5, 4, 7, 54, 76, 3, 54, 6, 76, 57, 58, 3)
