"""Homework2 - task4

Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы.

"""


in_str = 'Ab1cD e3fG Hij4 эюя'
lower, upper = 0, 0

for c in in_str:
    code = ord(c)
    if ord('a') <= ord(c) <= ord('z'):
        lower += 1
    elif ord('A') <= ord(c) <= ord('Z'):
        upper += 1

print('Input string:', in_str)
print('Number of upper en-letters: %s\nNumber of lower en-letters: %s' % (upper, lower))
