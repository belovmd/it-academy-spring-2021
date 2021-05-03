"""Homework2 - task7

Даны: три стороны треугольника. Требуется: проверить,
действительно ли это стороны треугольника. Если стороны
определяют треугольник, найти его площадь. Если нет,
вывести сообщение о неверных данных.
"""

a = float(input("Side a = "))
b = float(input("Side b = "))
c = float(input("Side c = "))

if a + b >= c and a + c >= b and b + c >= a:
    print("Triangle existed")
    semi_perimeter = (a + b + c) / 2
    x = (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)
    square = (semi_perimeter * x) ** 0.5

    print(square)
else:
    print("Triangle NOT existed")
