# Даны: три стороны треугольника. Требуется: проверить, действительно ли это
# стороны треугольника. Если стороны определяют треугольник, найти его площадь.
# Если нет, вывести сообщение о неверных данных.

Side_A = 5
Side_B = 5
Side_C = 5

if Side_A < Side_B + Side_C and Side_B < Side_A + Side_C and Side_C < Side_A + Side_B:
    Perimetr = (Side_A + Side_B + Side_C) / 2
    Square = (Perimetr * (Perimetr - Side_A) * (Perimetr - Side_B) * (Perimetr - Side_C))**.5
    print('Треуголиник. Площадь треугольника:', Square)
else:
    print('не треугольник. Данные не верны')
