# Task 5 — Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы
# один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N. Далее идет N
# чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
# которые знает i-й школьник.
# Пример входных данных:
# 3          # N количество школьников
# 2          # M1 количество языков первого школьника
# Russian    # языки первого школьника
# English
# 3          # M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3
# Russian
# Italian
# French
#
#
# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков. Затем - количество языков,
# которые знает хотя бы один школьник, на следующих строках - список таких
# языков.

import copy

input_languages, unique_languages = set(), set()
data_about_students = {}

for students in range(int(input("Number of students: "))):
    for num_of_languages in range(int(input("Languages of a new student: "))):
        input_languages.add(input("Language learned: "))
        data_about_students[students] = input_languages.copy()
    input_languages.clear()

for key, value in data_about_students.items():
    unique_languages.update(value)

common_language = unique_languages.copy()

for key, value in data_about_students.items():
    common_language.intersection_update(value)

print("Number of common languages:", len(common_language),
      "all students know:", common_language.pop(), sep="\n")

print("Number of languages that at least one student knows:",
      len(unique_languages))
[print(unique_languages.pop(), sep="\n") for _ in range(len(unique_languages))]
