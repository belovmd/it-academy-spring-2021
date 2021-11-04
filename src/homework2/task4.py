# Посчитать количество строчных (маленьких) и прописных (больших)
# букв в введенной строке. Учитывать только английские буквы.
str_ = 'Hello WorlD'
big_letter = 0
small_letter = 0
for i in str_:
    if 'A' <= i <= 'Z':
        big_letter += 1
    if 'a' <= i <= 'z':
        small_letter += 1

print('Прописные', big_letter)
print('Строчные', small_letter)
