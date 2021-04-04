"""
Треугольник.

Даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
"""


side_a = float(input('Введите длину первой стороны треугольнка : '))
side_b = float(input('Введите длину второй стороны треугольнка : '))
side_c = float(input('Введите длину третьей стороны треугольнка : '))

if side_a >= side_b + side_c or side_b >= side_a + side_c or side_c >= side_a + side_b:
    print('Неверные данные!')
else:
    perimeter = (side_a + side_b + side_c) / 2
    square = (perimeter * (perimeter - side_a) * (perimeter - side_b) * (perimeter - side_c)) ** 0.5
    print('Площадь данного треугольника : ', square)
