"""
Task5.

Языки
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.

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
В первой строке выведите количество языков,
которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""

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
