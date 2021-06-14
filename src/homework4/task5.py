# task4

# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные:
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
# которые знает i-й школьник.
# Выходные данные:
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков.
# Затем - количество языков, которые знает хотя бы один школьник,
# на следующих строках - список таких языков.

number_of_pupils = int(input())
number_of_languages = []
for pupil in range(number_of_pupils):
    number_of_languages.append(set())
    for _ in range(int(input())):
        number_of_languages[pupil].add(input())
at_least_one_student = set.intersection(*number_of_languages)
all_pupils = set.union(*number_of_languages)
print(len(all_pupils))
print(list(all_pupils))
print(len(at_least_one_student))
print(list(at_least_one_student))
