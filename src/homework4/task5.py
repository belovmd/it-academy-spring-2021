"""Homework 4 - Task 5"""

from io import TextIOBase


def students_languages(text_reader: TextIOBase) -> None:
    """Языки

    Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все
    школьники и языки, которые знает хотя бы один из школьников.
    Входные данные:
        Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi,
        после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й
        школьник.
    Выходные данные
        В первой строке выведите количество языков, которые знают все школьники. Начиная со
        второй строки - список таких языков. Затем - количество языков, которые знает хотя бы
        один школьник, на следующих строках - список таких языков.
    """
    sets_of_langs = []
    number_of_students = int(text_reader.readline().strip())
    for _ in range(number_of_students):
        number_of_languages = int(text_reader.readline().strip())
        sets_of_langs.append({text_reader.readline().strip() for _i in range(number_of_languages)})
    langs_intersection = set()
    langs_union = set()
    for langs_set in sets_of_langs:
        langs_intersection = (langs_intersection or langs_set) & langs_set
        langs_union |= langs_set
    print('All students know {} languages. They are:'.format(len(langs_intersection)))
    print(*langs_intersection, sep='\n')
    print(("The total number of languages that at least someone "
           "knows at school is {}. They are:").format(len(langs_union)))
    print(*langs_union, sep='\n')


if __name__ == '__main__':

    from io import StringIO

    input_text = """3
        2
        Russian
        English
        3
        Russian
        Belarusian
        English
        3
        Russian
        Italian
        French"""

    with StringIO(input_text) as reader:
        students_languages(reader)
