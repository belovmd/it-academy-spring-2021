# 2. Города
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

# Входные данные
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны. В следующей строке записано
# число M, далее идут M запросов — названия каких-то M городов,
# перечисленных выше.

# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится
# данный город.

# Примеры
# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa

# 3
# Odessa
# Moscow
# Novgorod

# Выходные данные
# Ukraine
# Russia
# Russia

# ------------------------------------------------------------------------------------ #

dct = {}
input_number_of_countries = int(input("Please, enter numbers of countries: "))  # 2
print("Entered number of countries:", input_number_of_countries)
while input_number_of_countries > 0:
    input_countries = input("Please, enter country name: ")
    input_cities = input("Please, enter city(-ies) name(s): ").split()
    dct.setdefault(input_countries, input_cities)  # append(input_cities) - для себя

    input_number_of_countries -= 1

input_M = int(input("Please, enter 'M' variable: "))
print("Entered 'M' variable:", input_M)
while input_M > 0:
    data_request = str(input("Please, enter city name: "))
    for key, value in dct.items():
        for elem in value:
            if elem == data_request:  # in или ==
                print(key)

    input_M -= 1

print(dct)
