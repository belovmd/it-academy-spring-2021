def homework4_task1():

    dct = {i: i ** 3 for i in range(1, 21)}
    print(dct)


def homework4_task2():

    dct_db = {}

    quantity_of_countries = int(input("Введите количество стран:\n"))

    while len(dct_db) != quantity_of_countries:
        user_input_lst = input("Введите страну и города:\n").split(" ")
        country, cities = user_input_lst[0], user_input_lst[1:]
        dct_db[country] = cities

    quantity_of_cities = int(input("Введите количество городов для поиска:\n"))

    cities_for_check = []

    while len(cities_for_check) != quantity_of_cities:
        cities_for_check.append(input("Введите город:\n"))

    for city in cities_for_check:
        for country in dct_db:
            if city in dct_db[country]:
                print(country)


def homework4_task3():

    lst1 = [1, 2, 5, 10, 8]
    lst2 = [2, 5, 17, 2, 4]

    print(len(set(lst1) & set(lst2)))


def homework4_task4():

    lst1 = [1, 2, 5, 10, 8]
    lst2 = [2, 5, 17, 2, 4]

    print(len(set(lst1) ^ set(lst2)))


def homework4_task5():

    lang_at_least_one_know = set()
    lang_each_know = set()

    num_of_students = int(input("введите количество школьников: "))

    for i in range(num_of_students):
        num_of_languages = int(input(f"введите количество языков {i + 1}го школьника: "))
        languages = set()

        while num_of_languages != len(languages):
            languages.add(input(f"введите язык Nr.{len(languages) + 1} для {i}го школьника: "))

        if not i:
            lang_each_know.update(languages)
        else:
            lang_each_know &= languages

        lang_at_least_one_know.update(languages)

    print(f"количество языков, которые знают все школьники: {len(lang_each_know)}")
    print(list(lang_each_know))
    print(f"количество языков, которые знает хотя бы один школьник {len(lang_at_least_one_know)}")
    print(list(lang_at_least_one_know))


def homework4_task6():
    str_1 = """Во входной строке записан текст.\n
    Словом считается последовательность непробельных символов идущих подряд,
    слова разделены одним или большим числом пробелов\n или символами конца строки.
    Определите, сколько различных слов\n содержится в этом тексте."""
    str_2 = "asd \n d   d"

    def count_unique_words(input_str):
        input_str = input_str.replace('\n', ' ')
        s = set(input_str.split(' '))
        s.discard('')
        return len(s)

    print(count_unique_words(str_1))
    print(count_unique_words(str_2))


def homework4_task7():
    num1 = 270
    num2 = 192

    while num1 % num2:
        num2, num1 = num1 % num2, num2

    print(num1 // num2)
