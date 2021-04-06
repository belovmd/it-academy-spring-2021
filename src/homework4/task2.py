"""Homework 4 - Task 2"""

from io import TextIOBase


def cities_query(text_reader: TextIOBase) -> None:
    """Города

    Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города
    укажите, в какой стране он находится.
    Входные данные:
        Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается
        с названия страны, затем идут названия городов этой страны. В следующей строке записано
        число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
    Выходные данные:
        Для каждого из запроса выведите название страны, в котором находится данный город.
    """
    countries = {}
    number_of_countries = int(text_reader.readline().strip())
    while number_of_countries:
        country, *cities = text_reader.readline().strip().split()
        if country and cities:
            countries[country] = cities
        number_of_countries -= 1
    number_of_queries = int(text_reader.readline().strip())
    while number_of_queries:
        query = text_reader.readline().strip()
        print(*[country for country, cities in countries.items() if query in cities])
        number_of_queries -= 1


if __name__ == '__main__':

    from io import StringIO

    input_text = """3
        Russia Moscow Petersburg Novgorod Kaluga
        Belarus Minsk Brest Gomel Grodno Mogilev Vitebsk
        France Paris Marseille Lyon Nice Cannes Brest
        3
        Cannes
        Petersburg
        Brest"""

    with StringIO(input_text) as reader:
        cities_query(reader)
