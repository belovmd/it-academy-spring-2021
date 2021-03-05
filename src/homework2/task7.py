"""Homework2 - task7

Даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.

"""


side1, side2, side3 = 15, 20, 12

perimeter = side1 + side2 + side3
max_side = max(side1, side2, side3)
if perimeter - max_side > max_side:
    print('Numbers %s, %s, %s are the sides of the triangle.' % (side1, side2, side3))
    hp = perimeter / 2
    S = (hp * (hp - side1) * (hp - side2) * (hp - side3)) ** 0.5   # Heron's formula
    print('S = ', S)
else:
    print('Numbers %s, %s, %s are NOT sides of the triangle.' % (side1, side2, side3))
