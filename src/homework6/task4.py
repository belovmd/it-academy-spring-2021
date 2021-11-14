from task3 import numbers

# TASK 75
# Оказывается, что 12 см - наименьшая длина проволоки, сгибая которую,
# можно получить прямоугольный треугольник с целыми сторонами, притом
# лишь единственным способом. Есть и другие примеры.
#
# 12 см: (3,4,5)
# 24 см: (6,8,10)
# 30 см: (5,12,13)
# 36 см: (9,12,15)
# 40 см: (8,15,17)
# 48 см: (12,16,20)
#
# В противоположность этим примерам, существуют такие длины проволоки (к примеру, 20 см),
# из которых нельзя получить прямоугольный треугольник с целыми сторонами. Другие же длины
# позволяют найти несколько возможных решений: к примеру, сгибая проволоку длинной 120 см,
# можно получить ровно три различных прямоугольных треугольника с целыми сторонами.
#
# 120 см: (30,40,50), (20,48,52), (24,45,51)
#
# Известно, что длина проволоки составляет L. Для скольких значений L ≤ 1 500 000,
# сгибая проволоку, можно получить ровно один прямоугольный треугольник с целыми сторонами?
#
# How it maid https://en.wikipedia.org/wiki/Pythagorean_triple


def triangle(wire):
    m = 2
    n = 1
    lst = []
    perimeter = 12

    while True:
        d = (m - n) % 2
        if perimeter > wire:
            n = n + 1
            m = n + 1

        if d == 1 and numbers(m, n) == 1:
            lst.append([m, n])
            m += 1
        else:
            m += 1

        perimeter = (m ** 2 - n ** 2) + (2 * m * n) + (m ** 2 + n ** 2)

        if m == (n + 2) and perimeter > wire:
            break

    dct = {}

    for i in range(len(lst)):
        m = lst[i][0]
        n = lst[i][1]
        perimeter = 12
        k = 1
        while perimeter <= wire:
            a = k * (m ** 2 - n ** 2)
            b = k * (2 * m * n)
            c = k * (m ** 2 + n ** 2)
            perimeter = a + b + c
            k += 1
            if perimeter <= wire:
                dct.setdefault(perimeter, []).append([a, b, c])

    triangles_numbers = 0

    for value in dct.values():
        if len(value) == 1:
            triangles_numbers += 1

    return triangles_numbers


triangle(1500000)