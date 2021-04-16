"""
Homework 4 - Task2"
Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные:
Программа получает на вход количество стран N. Далее идет N строк, каждая
строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия
каких-то M городов, перечисленных выше.
Выходные данные:
Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры:

Входные данные:
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

Выходные данные:
Ukraine
Russia
Russia
"""

dct_country_cities = {}
lst_cities = []

input_number_1 = int(input("Input number of countries: "))
for i in range(input_number_1):
    input_data = input("Input data: ")
    for n in range(1, len(input_data.split())):
        dct_country_cities.setdefault(input_data.split()[0], []).append(input_data.split()[n])

input_number_2 = int(input("Input number of cities: "))
for i in range(input_number_2):
    lst_cities.append(input("Input city: "))

for city in lst_cities:
    for key, value in dct_country_cities.items():
        if city in value:
            print(key)
