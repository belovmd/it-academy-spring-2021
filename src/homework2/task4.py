"""Homework2 - task4

Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы.

"""


in_str = 'Abгd d2пE Fgычk07дvXXyY zЯЯ'
en_lower = 'etaoinshrdlcumwfgypbvkxjqz'   # lower en-letters in order of frequency
en_upper = 'ETAOINSHRDLCUMWFGYPBVKXJQZ'   # upper en-letters in order of frequency
lower_num = 0
upper_num = 0

for c in in_str:
    if c in en_lower:
        lower_num += 1
    elif c in en_upper:
        upper_num += 1

print('Input string:', in_str)
print('Number of upper en-letters: %s\nNumber of lower en-letters: %s' % (upper_num, lower_num))
