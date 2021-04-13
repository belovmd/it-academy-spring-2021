# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк,
# каждая строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия каких-то M
# городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.
# Примеры

number_city = int(input("Введите количество стран:"))
base_country_city = {}
city_list = []

for key_country in range(1, number_city + 1):
    s = input("Вводите страну, а затем название городов:")
    d = s.split()
    base_country_city[d[0]] = d[1:]

revers_base = dict((v, k) for k, val in base_country_city.items() for v in val)
what_country = int(input('Количество?:'))
for questions in range(1, what_country + 1):
    what_city = (input('Введите город:'))
    city_list.append(what_city)
for answer in city_list:
    print(revers_base.get(answer))
