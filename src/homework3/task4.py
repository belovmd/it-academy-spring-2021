# 4. Пары элементов
# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

input_data = list('1 1 1 1')  # [1, ' ', 1, ' ', 1]
print("Entered data in list: ", input_data)
input_data2 = ','.join(input_data)
print(input_data2)
work_data = input_data2.replace(', ', '')
print(work_data)
work_data = work_data.replace(',', '')
print("Entered data: ", work_data)
print(len(work_data))

pairs1 = 0
for x in range(len(work_data)):
    for y in range(x+1, len(work_data)):
        if work_data[x] == work_data[y]:
            print("x-", x, ";", "y-", y)
            print(work_data[x], work_data[y])
            pairs1 += 1
    print()

print("1st FOR range:", range(len(work_data)))
print("Glimpse on the first range for the 1st FOR:", list(range(len(work_data))))
print("Length of the 1st FOR range:", len(work_data))
print()

q = len(work_data)
print("2nd FOR range:", range(1, q))
print("Glimpse on the second range for the 2nd FOR:", list(range(1, q)))
print("Length of the 2nd FOR range:", len(range(1, q)))
print()

print("Number of pairs:", pairs1)
