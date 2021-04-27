# Пары элементов
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо
# посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

str1 = '1 2 3 3 2 4 1 33 '
lst = str1.split()
print(lst)
num_pair = 0
for first_num in range(len(lst)):
    for sec_num in range(first_num + 1, len(lst)):
        if lst[first_num] == lst[sec_num]:
            num_pair += 1

print(num_pair)
