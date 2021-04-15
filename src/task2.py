# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк,
# каждая строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия каких-то M городов,
# перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.

str1 = "Russia Moscow Petersburg Novgorod Kaluga"
str2 = "Ukraine Kiev Donetsk Odessa"

country1, *cities1 = str1.split()
country2, *cities2 = str2.split()
dct1 = {city: country1 for city in cities1}
dct2 = {city: country2 for city in cities2}
dct1.update(dct2)

print(dct1[input("Enter city: ")])
print(dct1[input("Enter city: ")])
print(dct1[input("Enter city: ")])
