# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
# которые знает i-й школьник.
# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков. Затем - количество языков,
# которые знает хотя бы один школьник, на следующих строках - список таких языков.

N = input("Enter the number of students: ")
M1 = input("Enter the number of languages of the first student: ")
Languages1 = (input("Enter the languages of the first students: ")).split()
Languages1 = set(Languages1)

M2 = input("Enter the number of languages of the second student: ")
Languages2 = (input("Enter the languages of the second students: ")).split()
Languages2 = set(Languages2)

M3 = input("Enter the number of languages of the third  student: ")
Languages3 = (input("Enter the languages of the third  students: ")).split()
Languages3 = set(Languages3)

all_students = Languages1 & Languages2 & Languages3
one_student = Languages1 | Languages2 | Languages3

print(len(all_students), *all_students, len(one_student), *one_student, sep='\n')
