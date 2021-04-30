'''
Каждый из N школьников некоторой школы знает
Mi языков. Определите, какие языки знают все
школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество
школьников N. Далее идет N чисел Mi, после каждого
из чисел идет Mi строк, содержащих названия
языков, которые знает i-й школьник.
Пример входных данных:
3          # N количество школьников
2          # M1 количество языков первого школьника
Russian    # языки первого школьника
English
3          # M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French
Выходные данные
В первой строке выведите количество языков, которые з
нают все школьники. Начиная со второй строки - список
таких языков. Затем - количество языков, которые знает хотя бы
один школьник, на следующих строках - список таких языков.
'''


def enter_data():
    print("Входные данные")
    count_student = int(input())
    dict_stud_lang = {}
    while count_student:
        count_languages = int(input())
        set_ = set()
        while count_languages:
            language = input()
            set_.add(language)
            count_languages -= 1
        dict_stud_lang[count_student] = set_
        count_student -= 1
    return dict_stud_lang


def show_data(common_lan, all_lan):
    print("Выходные данные")
    print(len(common_lan))
    for elem in common_lan:
        print(elem)
    print(len(all_lan))
    for elem in all_lan:
        print(elem)


dict_stud_lang = enter_data()
common_languages = dict_stud_lang.popitem()[1]
all_languages = common_languages.copy()
for key, value in dict_stud_lang.items():
    common_languages &= value
for key, value in dict_stud_lang.items():
    all_languages |= value
show_data(common_languages, all_languages)
