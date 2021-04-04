"""
Строчные и прописные.

Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

my_str = input('Введите строку : ')

lowercase_counter = len([ch_ for ch_ in my_str if 'a' <= ch_ <= 'z'])
uppercase_counter = len([ch_ for ch_ in my_str if 'A' <= ch_ <= 'Z'])

print('Строчных : {}. Прописных : {}'.format(lowercase_counter, uppercase_counter))
