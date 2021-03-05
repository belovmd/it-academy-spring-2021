# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке
str = 'Python string method split() inputs a string value and ' \
      'outputs a list of words contained within ' \
      'the string by separating or splitting the words ' \
      'on all the whitespaces by default. It also has an ' \
      'optional Argument for limiting the number of splits.'
big = 0
small = 0

for i in str:
    if 'A' <= i <= 'Z':
        big += 1
    elif 'a' <= i <= 'z':
        small += 1
        continue

print('колличество больших букв =', big)
print('колличество маленьких букв =', small)
