import re

my_string = input('Посчитать количество строчных (маленьких) и прописных (больших)\n'
                  'букв в введенной строке. Учитывать только английские буквы.')

my_string = re.sub(r'[^A-z]', '', my_string)
print(my_string)

low = 0
up = 0
i = 0
for i in my_string:
    if i.islower():
        low += 1
    else:
        up += 1

print('Маленькие =', low, 'большие =', up)

print('Большие', sum(map(str.isupper, my_string)), 'маленькие', sum(map(str.islower, my_string)))
