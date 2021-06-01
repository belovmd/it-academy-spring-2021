"""
Языки

Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""


num_of_schoolboys = int(input())
schoolboy_lang = {}
all_lang = set()


while num_of_schoolboys:
    num_of_lang = int(input())
    schoolboy_lang[num_of_schoolboys] = set()
    while num_of_lang:
        lang_ = input()
        all_lang.add(lang_)
        schoolboy_lang[num_of_schoolboys].add(lang_)
        num_of_lang -= 1
    num_of_schoolboys -= 1


general_lang = all_lang.copy()
for lang in schoolboy_lang.values():
    general_lang &= lang

un_lang = all_lang.copy()
for lang in schoolboy_lang.values():
    un_lang |= lang


print(len(general_lang), *general_lang, sep='\n')
print(len(un_lang), *un_lang, sep='\n')
