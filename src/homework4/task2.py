"""
Города

Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов,
перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.
"""


num_of_countries = int(input())
data = {}
while num_of_countries > 0:
    country, *sities = input().split()
    data[country] = sities
    num_of_countries -= 1

requests = []
num_of_requests = int(input())
while num_of_requests:
    requests.append(input())
    num_of_requests -= 1

for request in requests:
    for country in data.keys():
        if request in data[country]:
            print(country)
