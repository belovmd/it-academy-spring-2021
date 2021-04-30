"""Города

Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
"""

# input data
countries_num = int(input("Введите количество стран: "))
dict_ = {}

# make database wih dict
for num in range(countries_num):
    country, *cities = input().split()
    dict_[country] = cities

# requests
requests_num = int(input("Введите число запросов: "))
requests_lst = []
for _ in range(requests_num):
    requests_lst.append(input())

# output data
for city in requests_lst:
    for key, value in dict_.items():
        if city in value:
            print(key)
