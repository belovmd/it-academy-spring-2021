# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

string = 'AasdA ddfds sdAASdDFD'
n, v = 0, 0
for char in string:
    if char.islower():
        n += 1
    elif char.isupper():
        v += 1
print('В нижнем регистре:', n, '\nВ верхнем регистре:', v)
