# 5. Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
#
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
# содержащих названия языков, которые знает i-й школьник.
#
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
# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков.
# Затем - количество языков, которые знает хотя бы один школьник,
# на следующих строках - список таких языков.

# ------------------------------------------------------------------------------------ #

number_of_pupils = int(input("Please, enter total amount of pupils: ", ))
all_pupils_languages = []
number_of_languages = []

count_for_while = 1
while count_for_while <= number_of_pupils:
    number_of_languages = input('Please, enter amount of learned languages by pupil: ', )
    for i in range(1, len(number_of_languages) + 1):
        input_languages = input("Please, enter names of languages (use 'space' as separator): ", ).split()
        all_pupils_languages.append(input_languages)
    count_for_while += 1

pupils_languages = [set(i) for i in all_pupils_languages]
# print("all_pupils_languages - set: ", pupils_languages)

# 1
all_known_language = set.intersection(*pupils_languages)
# print("*pupils_languages: ", *pupils_languages)
print("Amount of learned languages by every pupil: ", len(all_known_language))
print("Language(-s) which is (are) learned by all pupils is (are): ", sorted(all_known_language))

# 2
each_pupil_lang = set.union(*pupils_languages)
# print("*pupils_languages: ", *pupils_languages)
print("Amount of languages which at least 1 pupil knows: ", len(each_pupil_lang))
print("Languages list which at least 1 pupil knows: ", sorted(each_pupil_lang))
