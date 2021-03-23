"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

str_ = str(input('Введите строку:'))
lowercase_number = 0
uppercase_number = 0

for letter in str_:
    if 'a' <= letter <= 'z':
        lowercase_number += 1
    elif 'A' <= letter <= 'Z':
        uppercase_number += 1

print('Количество строчных (маленьких) букв: ', lowercase_number)
print('Количество прописных (больших) букв: ', uppercase_number)
