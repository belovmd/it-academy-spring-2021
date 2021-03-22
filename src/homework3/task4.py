import random

random.seed(4400)


def calculate_count_of_pairs(count_num):
    count_of_pairs = 0
    while count_num:
        count_num -= 1
        count_of_pairs += count_num
    return count_of_pairs


def find_repeat_numbers(lst_):
    repeat_numbers = []
    pair_of_numbers = dict()
    for elem in lst_:
        if elem not in repeat_numbers and lst_.count(elem) > 1:
            repeat_numbers.append(elem)
            count = lst_.count(elem)
            pair_of_numbers[elem] = calculate_count_of_pairs(count)
    return pair_of_numbers


def print_pair_of_numbers(pair_of_numbers):
    print()
    print("|{column1:^16}|{column2:^16}|".format(column1="Элемент", column2="Количество пар"))
    for key, item in pair_of_numbers.items():
        print("|{key:^16}|{item:^16}|".format(key=key, item=item))


lst_ = [random.randint(1, 6) for num in range(0, 15)]
print("Исходный список:", *lst_)
print_pair_of_numbers(find_repeat_numbers(lst_))
