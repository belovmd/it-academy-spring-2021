# Task 4. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных
# друг другу. Любые два элемента, равные друг другу образуют одну пару,

numbers = [int(num) for num in input("Введите числа: ").split()]
pairs = 0

for element1 in range(len(numbers)):
    for element2 in range(element1 + 1, len(numbers)):
        if numbers[element1] == numbers[element1]:
            pairs += 1

print(pairs)
