# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города
# укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается
# с названия страны, затем идут названия городов этой страны. В следующей строке записано
# число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.
# Примеры
#
# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
#
# 3
# Odessa
# Moscow
# Novgorod
#
# Выходные данные
# Ukraine
# Russia
# Russia

Num_countries = int(input('Введите количество стран: '))
print('Количество стран: ', Num_countries)
dct = {}

for num in range(Num_countries):
    country = str(input('Введите страну: '))
    cities = str(input('Введите города этой страны через пробел: ')).split()
    dct[country] = cities

request = int(input('Введите количество запросов: '))

for num_request in range(request):
    city = input('Введите город поиска: ')
    for country, cities in dct.items():
        if city in cities:
            print(country)
