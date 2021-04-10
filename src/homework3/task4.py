# Пары элементов
# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар


def count_pairs(str_):
    dict_ = {}

    for elem in str_.split(' '):
        if elem not in dict_:
            dict_[elem] = 0
        dict_[elem] += 1

    for elem in dict_:
        pairs = sum(range(dict_[elem]))
        if pairs > 0:
            print("Element {} has {} pair(s)".format(elem, pairs))


print(count_pairs("1 1 2 5 2 7 9 10 10 1 1 1"))
