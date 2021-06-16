"""
Task2.

Города
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов —
названия каких-то M городов, перечисленных выше.

Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.

Примеры

Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa

3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
"""

dct_db = {}

quantity_of_countries = int(input("Введите количество стран:\n"))

while len(dct_db) != quantity_of_countries:
    country, *cities = input("Введите страну и города:\n").split(" ")
    dct_db[country] = cities

quantity_of_cities = int(input("Введите количество городов для поиска:\n"))

cities_for_check = []

while len(cities_for_check) != quantity_of_cities:
    cities_for_check.append(input("Введите город:\n"))

for city in cities_for_check:
    for country in dct_db:
        if city in dct_db[country]:
            print(country)
