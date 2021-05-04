"""Homework 4 - Task5

Языки
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""

from functools import reduce

dct_pupil_languages = {}

input_number_1 = int(input("Input number of pupils: "))
for pupil_number in range(1, input_number_1 + 1):
    dct_pupil_languages.setdefault(pupil_number, set())

for key, value in dct_pupil_languages.items():
    input_number_2 = int(input("Input number of languages " + str(key) + " pupil: "))
    for i in range(input_number_2):
        input_language = (input("Input language: "))
        dct_pupil_languages.setdefault(key, set()).add(input_language)

every_lang = reduce(lambda x, y: x & y, dct_pupil_languages.values())
all_lang = reduce(lambda x, y: x | y, dct_pupil_languages.values())

print(len(every_lang), list(every_lang), sep='\n')
print(len(all_lang), list(all_lang), sep='\n')
