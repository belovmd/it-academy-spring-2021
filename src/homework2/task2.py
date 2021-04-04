# Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
str_ = 'Привет, безумный мир.'
k = str_.replace('.', '')
k2 = k.replace(',', '')
k3 = k2.split()
count = 0

for i in k3:
    if len(i) > count:
        count = len(i)
print(count)
