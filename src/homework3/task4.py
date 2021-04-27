import random

random.seed(4400)


def calculate_count_of_pairs(lst_):
    cache = dict()
    for elem in set(lst_):
        count_ = lst_.count(elem)
        cache[elem] = count_ * (count_ - 1) - sum(range(count_))
    return cache


def print_pair_of_numbers(pair_of_numbers):
    print()
    print("|{column1:^16}|{column2:^16}|".format(column1="Элемент", column2="Количество пар"))
    for key, item in pair_of_numbers.items():
        print("|{key:^16}|{item:^16}|".format(key=key, item=item))


lst_ = [random.randint(1, 6) for num in range(0, 15)]
print("Исходный список:", *lst_)
print_pair_of_numbers(calculate_count_of_pairs(lst_))
