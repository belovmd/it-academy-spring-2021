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

languages = []
data_about_students = {}

for students in range(int(input("Number of students: "))):
    for num_of_languages in range(int(input("Languages of a new student: "))):
        language = input("Language learned: ")
        languages.append(language)
        copy_for_dict = copy.deepcopy(languages)
    data_about_students[students] = copy_for_dict
    languages.clear()

# for checking lines 32-40:
# data_about_students = {0: ['ru', 'eng'], 1: ['ru', 'bel', 'eng'],
#                        2: ['ru', 'fr', 'it']}

working_set_of_langs = set(data_about_students[0])

for key, value in data_about_students.items():
    working_set_of_langs.intersection_update(set(value))

print("Number of common languages:", len(working_set_of_langs))
print("All students know:", working_set_of_langs.pop())

working_set_of_langs = set(data_about_students[0])

for key, value in data_about_students.items():
    working_set_of_langs.update(set(value))

print("Number of languages that at least one student know:",
      len(working_set_of_langs))

num_of_iterations = len(working_set_of_langs)
for _ in range(num_of_iterations):
    print(working_set_of_langs.pop())
