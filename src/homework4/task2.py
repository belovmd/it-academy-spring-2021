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
country_lst = []
dict_ = {}

for num in range(countries_num):
    country_lst.append(input().split())

# make database wih dict
dict_ = {country_lst[num][0]: country_lst[num][1:] for num in range(countries_num)}

# requests
requests_num = int(input("Введите число запросов:"))
requests_lst = []
for _ in range(requests_num):
    requests_lst.append(input())


# output data
for city in requests_lst:
    for num in range(countries_num):
        if city in list(dict_.values())[num]:
            for key in dict_:
                if city in dict_[key]:
                    print(key)
                else:
                    pass
        else:
            pass
