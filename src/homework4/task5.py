"""Языки

Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
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
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""

# input data
students_amount = int(input("Введите количество школьников: "))
counter = students_amount
langs = {}

while counter:
    lang_amount = int(input("Введите количество языков, которое знает школьник: "))
    lang_student = (input("Введите язык: ") for _ in range(lang_amount))
    langs[students_amount - counter + 1] = set(lang_student)
    counter -= 1

# output data
# all known languages
student_langs = langs[1]
for lang in langs.values():
    student_langs = student_langs | lang
print(len(student_langs))
for lang in student_langs:
    print(lang)

# languages which know every students
every_body_lang = langs[1]
for lang in langs.values():
    every_body_lang = every_body_lang & lang
print(len(every_body_lang))
if len(every_body_lang):
    for lang in every_body_lang:
        print(lang)
else:
    print("No these languages")
