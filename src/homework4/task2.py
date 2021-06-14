# task2

# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк,
# каждая строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.

number_of_countries = int(input())
dict_world = {}
for number in range(number_of_countries):
    country = input().split()
    dict_new_country = dict.fromkeys(country[1:], country[0])
    dict_world.update(dict_new_country)
number_of_requests = int(input())
for request in range(number_of_requests):
    city = input()
    print(dict_world[city])
