# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# в которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
# lst = [1, 8, 2, 3, 5, 5, 7, 3, 2, 2, 1, 8]
lst_new = []
element = 0
count = 0

print('Введите числа через пробел:')
str_new = input()
lst = str_new.split()

while element < len(lst):
    count = element + 1
    while count < len(lst):
        if lst[element] == lst[count]:
            lst_new.append(lst[element])
            count += 1
        else:
            count += 1
    element += 1

print('колличество пар = ', len(lst_new))
