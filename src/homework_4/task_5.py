# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих
# названия языков, которые знает i-й школьник.

# Пример входных данных:
# 	3          # N количество школьников
# 2          # M1 количество языков первого школьника
# Russian    # языки первого школьника
# English
# 3          # M2 количество языков второго школьника
# Russian
# Belarusian
# English

lang = []
number_pupil = int(input("Введите количество школьников:"))
pupil_experience = {i: [] for i in list(range(1, number_pupil + 1))}

for key_pupil in range(1, number_pupil + 1):
    number_language = int(input("Количество языков школьника:"))
    for key_languages in range(1, number_language + 1):
        pupil_experience[key_pupil].append(input("Какой язык?:"))

for key in pupil_experience.values():
    lang.extend(key)

print(*list(set(lang)), sep=', ')

uniq_list = [uniq for uniq in lang if lang.count(uniq) == 1]

print(*uniq_list)
