# 7. Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь.
# Если нет, вывести сообщение о неверных данных.


A = 8
B = 9
C = 10
# p = (A+B+C)//2 # semi-perimeter
# S = (abs(p*(p-A)*(p-B)*(p-C)))**0.5 # area
if A < B + C and B < A + C and C < A + B:
    print ("A, B, C - sides of a triangle")
    #print ((A + B + C) // 2)
    print ("Area of a triangle:", (abs(
        ((A + B + C) // 2) * (((A + B + C) // 2) - A) * (((A + B + C) // 2) - B) * (((A + B + C) // 2) - C))) ** 0.5)
else:
    print ("Wrong data")