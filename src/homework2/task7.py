# Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны
# треугольника. Если стороны определяют треугольник, найти его площадь.
# Если нет, вывести сообщение о неверных данных.
side1 = 40
side2 = 60
side3 = 80
p = (side1 + side2 + side3) / 2  # semi-perimeter for square

if (side2 - side3) < side1 < (side2 + side3):
    if (side1 - side3) < side2 < (side1 + side3):
        if (side1 - side2) < side3 < (side1 + side2):
            S = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
            print("Площадь треугольника равна", S)
        else:
            print("Неверные данные")
    else:
        print("Неверные данные")
else:
    print("Неверные данные")
