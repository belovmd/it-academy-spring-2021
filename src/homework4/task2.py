"""
Города

Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
"""


# str1 = 'Russia Moscow Petersburg Novgorod Kaluga'
# str2 = 'Ukraine Kiev Donetsk Odessa'
# request_1 = 'Odessa'
# request_2 = 'Moscow'
# request_3 = 'Novgorod'


dct = {}


def make_a_dict(n):
    while n > 0:
        str_ = input('Введите название страны и городов:')
        lst = list(str_.split(' '))
        key, value = lst[0], lst[1:]
        dct[key] = value
        n -= 1
    # print(dct)


def find_country(m):
    while m > 0:
        city = input('Введите название города:')
        for k, v in dct.items():
            if city in v:
                print(k)
        m -= 1


make_a_dict(int(input('Введите количество стран N:')))
find_country(int(input('Введите количество запросов M:')))
