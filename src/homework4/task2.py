'''
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
 затем идут названия городов этой страны. В следующей
строке записано число M, далее идут M запросов —
названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
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
'''


def enter_data():
    count_iter = int(input())
    lst_ = []
    while count_iter:
        str_ = input()
        lst_.append(str_)
        count_iter -= 1
    return lst_


def separate_country_and_cities(lst_):
    dict_ = {}
    for elem in lst_:
        pos = elem.find(" ")
        dict_[elem[: pos + 1]] = elem[pos + 1:]
    return dict_


def find_countries(dict_countries, lst_cities):
    lst_countries = []
    for city in lst_cities:
        for country, cities_of_country in dict_countries.items():
            if city in cities_of_country:
                lst_countries.append(country)
    return lst_countries


def print_result():
    print("Входные данные")
    lst_country_and_cities = enter_data()
    country_and_cities = separate_country_and_cities(lst_country_and_cities)
    lst_cities = enter_data()
    lst_countries = find_countries(country_and_cities, lst_cities)
    print("\nВыходные данные")
    print(*lst_countries, sep="\n")


print_result()
