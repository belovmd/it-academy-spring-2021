# Task 7. Даны: три стороны треугольника. Требуется: проверить, действительно
# ли это стороны треугольника. Если стороны определяют треугольник, найти его
# площадь. Если нет, то вывести сообщение о неверных данных.

the_sides = input("Введите 3 числа через пробел: ").split()

# the_sides is the list of 3 numbers which are in a format of strings,
# "a", "b", "c" are names for the sides of a triangle.

a, b, c = int(the_sides[0]), int(the_sides[1]), int(the_sides[2])

if a + b > c and a + c > b and b + c > a:
    semi = (a + b + c) / 2                  # semiperimeter
    area = (semi * (semi - a) * (semi - b) * (semi - c)) ** 0.5
    print("Площадь треугольника =", area)

else:
    print("Неверные данные")
