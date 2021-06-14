# Реализовать функцию get_ranges,
# которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”.

def get_ranges(list_):
    before_number = list_[0]
    temporary_list = [list_[0]]
    for number in list_:
        if number == list_[0]:
            continue
        elif before_number + 1 == number:
            temporary_list.append(number)
            before_number = number
        elif True:
            if len(temporary_list) == 1:
                print(before_number, end=',')
            else:
                print(f'{temporary_list[0]}-{temporary_list[-1]}', end=',')
                temporary_list.clear()
                temporary_list.append(number)
            before_number = number
    if len(temporary_list) == 1:
        print(list_[-1])
    else:
        print(f'{temporary_list[0]}-{temporary_list[-1]}')


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
